from django.conf.urls import patterns, include, url

urlpatterns = patterns('webpage.views',
    url(r'^$', 'index', {}, 'index'),

    url(r'^host_party/$', 'host_party', {}, 'host_party'),

)