from django.conf.urls import patterns, url
from backend import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^host_party$', views.host_party, name='host_party'),
    url(r'^join_party$', views.join_party, name='join_party'),
    url(r'^player$', views.player, name='player'),
)