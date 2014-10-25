from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'webpage.views.index', {}, 'index'),

    url(r'^player/', include('webplayer.urls')),
    url(r'^webparty/', include('webparty.urls', namespace="webparty")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^backend/', include('backend.urls', namespace="backend")),
)
