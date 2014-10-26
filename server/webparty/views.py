import urllib
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from backend.models import Song
from backend.views import get_user


def index(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
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
        }
        return render(request, "webparty/index.html", context)

    return render(request, "webparty/index.html")


def enqueue_song(request):
    song = Song(service_id=request.POST.get('songid'), name=request.POST.get('songname'))
    song.save()
    user = get_user(request)
    user.party.songs.add(song)
    user.save()

    return HttpResponse(status=204)