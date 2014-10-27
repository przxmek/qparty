from django.conf.urls import patterns, include, url

from webplayer import views

urlpatterns = patterns('webplayer.views',
    url(r'^$', 'player', {}, 'player'),
    url(r'^playlist/$', views.playlist, name='playlist'),
    url(r'^playlist/votes/$', views.playlist, {'template_name': 'webplayer/playlist_votes.html'}),
    url(r'^next_song/$', views.next_song, name='next_song'),
    url(r'^pop_song/$', views.pop_song, name='pop_song')
)
