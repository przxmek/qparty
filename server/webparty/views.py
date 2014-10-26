import urllib
from bs4 import BeautifulSoup
import json
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from backend.models import Song
from backend.views import get_user, is_party_assigned


def index(request):
    if not is_party_assigned(request):
        return redirect('webpage:index')

    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query == '':
            return render(request, "webparty/index.html")

        encoded_query = urllib.parse.urlencode({'search_query': search_query})
        response = urllib.request.urlopen('https://www.youtube.com/results?' + encoded_query)
        page_src = response.read()
        response.close()
        parsed = BeautifulSoup(page_src)

        search_results = []
        div_results = parsed.body.find('div', attrs={'id': 'results'})
        songs_divs = div_results.find_all('div', attrs={'class': 'yt-lockup-content'})
        for div in songs_divs:
            link = div.find('a')
            search_results.append((link.get('href')[9:], link.text))

        context = {
            'search_query': search_query,
            'search_results': search_results,
            'user': get_user(request),
        }
        return render(request, "webparty/index.html", context)

    return render(request, "webparty/index.html", {'user': get_user(request)})


def enqueue_song(request):
    if not is_party_assigned(request):
        return redirect('webpage:index')

    song = Song(service_id=request.POST.get('songid'), name=request.POST.get('songname'))
    song.save()
    user = get_user(request)
    user.party.songs.add(song)
    user.save()

    return HttpResponse(status=204)


def upvote(request, song_id=-1):
    if not is_party_assigned(request):
        raise Http404

    user = get_user(request)
    song = user.party.songs.get(pk=song_id)
    user.upvote_song(song)

    return HttpResponse(json.dumps((song.pk, song.voting_result)), content_type="application/json")


def downvote(request, song_id=-1):
    if not is_party_assigned(request):
        raise Http404

    user = get_user(request)
    song = user.party.songs.get(pk=song_id)
    user.downvote_song(song)

    return HttpResponse(json.dumps((song.pk, song.voting_result)), content_type="application/json")
