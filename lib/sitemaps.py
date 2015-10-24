from django.contrib.sitemaps import Sitemap

from news.models import News
from pages.models import Pages
from events.models import Fighters, Events

class NewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return News.objects.filter(status__in=[3,4])
    
class PagesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Pages.objects.filter(enable=1)
    
class FightersSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4

    def items(self):
        return Fighters.objects.all()
    
class EventsTopSitemap(Sitemap): # Актуальные события
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Events.objects.filter(archive=0)
    
class EventsArchiveSitemap(Sitemap): # Архивные события
    changefreq = "never"
    priority = 0.3

    def items(self):
        return Events.objects.filter(archive=1)