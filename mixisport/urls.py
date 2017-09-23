from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from lib.sitemaps import *

from photologue.views import GalleryListView

from django.conf.urls.static import static

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
    url(r'^galleries/', GalleryListView.as_view(paginate_by=10), name='galleries'),
    url(r'^video/', include('videos.urls')),
    url(r'^', include('news.urls')),

    #   
    url(r'^redactor/', include('redactor.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^gallery/', include('photologue.urls', namespace='photologue')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)