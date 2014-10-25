from django.conf.urls import patterns, include, url

urlpatterns = patterns('webplayer.views',
    url(r'^$', 'player', {}, 'player')
)
