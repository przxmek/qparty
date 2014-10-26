from django.conf.urls import patterns, url
from youtube import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)