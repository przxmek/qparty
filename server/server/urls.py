from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^player/', include('webplayer.urls')),
    url(r'^webparty/', include('webparty.urls', namespace="webparty")),

    url(r'^admin/', include(admin.site.urls)),
)
