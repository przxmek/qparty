from django.http.response import Http404
from django.shortcuts import render
import json
from django.http import HttpResponse


def player(request, template_name='webplayer/player.html'):
    context = {

    }

    return render(request, template_name, context)


def playlist(request):
    if not request.is_ajax():
        raise Http404
    songs_list = [('a', 'aa'), ('b', 'bb'), ('c', 'cc')]
    return render(request, 'webplayer/playlist.html', {'songs_list': songs_list})


def next_song(request):
    if not request.is_ajax():
        raise Http404
    next = 'mCjtUXRJ57o'
    return HttpResponse(json.dumps(next), content_type="application/json")