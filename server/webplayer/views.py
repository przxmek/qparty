from django.http.response import Http404
from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from backend.views import is_party_assigned, get_user


def player(request, template_name='webplayer/player.html'):
    if not is_party_assigned(request):
        raise Http404

    user = get_user(request)

    context = {
        'user': user,
    }

    return render(request, template_name, context)


def playlist(request, template_name='webplayer/playlist.html'):
    if not request.is_ajax():
        raise Http404

    if not is_party_assigned(request):
        raise Http404

    user = get_user(request)
    songs_list = user.party.songs.order_by('-voting_result')[1:]

    return render(request, template_name, {'songs_list': songs_list})


def next_song(request):
    if not request.is_ajax():
        raise Http404

    if not is_party_assigned(request):
        raise Http404

    user = get_user(request)
    next = user.party.songs.order_by('-voting_result')[0]
    next.voting_result = 20000
    next.save()

    return HttpResponse(json.dumps(next.service_id), content_type="application/json")


def pop_song(request):
    if not request.is_ajax():
        raise Http404

    if not is_party_assigned(request):
        raise Http404

    user = get_user(request)
    user.party.songs.order_by('-voting_result')[0].delete()

    return HttpResponse(status=204)