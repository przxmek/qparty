from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^player/', include('webplayer.urls')),
    url(r'^webparty/', include('webparty.urls', namespace="webparty")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^backend/', include('backend.urls', namespace='backend')),
    url(r'^youtube/', include('youtube.urls', namespace='youtube')),
    url(r'^', include('webpage.urls', namespace="webpage")),
)
