from django.contrib.sitemaps import Sitemap

from news.models import News
from pages.models import Pages

class NewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return News.objects.filter(status__in=[3,4])
    
class PagesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Pages.objects.filter(enable=1)