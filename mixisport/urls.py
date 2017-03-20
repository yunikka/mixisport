from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from lib.sitemaps import *

sitemaps = {
    'news': NewsSitemap(),
    'pages': PagesSitemap(),
    'fighters': FightersSitemap(),
    'eventstop': EventsTopSitemap(),
    'eventsarchive': EventsArchiveSitemap(),
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^', include('news.urls')),

    #   
    url(r'^redactor/', include('redactor.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^chaining/', include('smart_selects.urls')),
    
]
