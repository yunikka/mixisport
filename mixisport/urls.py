from django.conf.urls import include, url, patterns
from django.contrib import admin
from filebrowser.sites import site
from django.conf import settings
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
    url(r'^$', include('news.urls')),
]



urlpatterns += patterns('',
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^chaining/', include('smart_selects.urls')),
)