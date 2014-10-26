from django.conf.urls import patterns, include, url

from webparty import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^enqueue_song$', views.enqueue_song, name='enqueue_song'),
                       url(r'^upvote/(?P<song_id>\d+)/$', views.upvote),
                       url(r'^downvote/(?P<song_id>\d+)/$', views.downvote)
)
