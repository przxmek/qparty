from django.conf.urls import patterns, include, url

from webparty import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^enqueue_song$', views.enqueue_song, name='enqueue_song'),
)
