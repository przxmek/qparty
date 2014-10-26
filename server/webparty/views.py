from django.http import HttpResponse, Http404
from django.shortcuts import render
import json
from backend.views import is_party_assigned, get_user

# Create your views here.


def index(request):
    return render(request, "webparty/index.html")


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