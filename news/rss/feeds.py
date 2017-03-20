from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils import timezone
import datetime
import re
from django.shortcuts import get_object_or_404

from news.models import News, Category
from piece.models import Seo

class DefaultRSS(Feed):
    try:
        title = Seo.objects.get(tag=1)
    except:
        title = None
    try:
        description = Seo.objects.get(tag=2)
    except:
        description = None

    link = "/"

    def items(self):
        return News.objects.filter(status__in=[3,4]).order_by('-created')[:30]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        return item.content
    
class RSS_limit_content(Feed):
    try:
        title = Seo.objects.get(tag=1)
    except:
        title = None
    try:
        description = Seo.objects.get(tag=2)
    except:
        description = None

    link = "/"

    def items(self):
        return News.objects.filter(status__in=[3,4]).order_by('-created')[:30]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        result = re.findall(r'^.*?<br>', item.content)
        # Если регулярное выражение ничего не нашло, значит в контенте нет <br> и просто отдаем весь контент
        if len(result) == 0:
            result = item.content
        else:
            result = result[0]
        return result
        #return item.content

class SocialRSS(Feed):
    try:
        title = Seo.objects.get(tag=1)
    except:
        title = None

    link = "/"

    def items(self):
        return News.objects.filter(status__in=[3,4]).filter(created__gt=(timezone.now() - datetime.timedelta(days=1))).order_by('-created')
    
class BodibildingRSS(Feed):
    try:
        title = Seo.objects.get(tag=1)
    except:
        title = None

    link = "/"

    def items(self):
        category = get_object_or_404(Category, slug='bodibilding')
        return News.objects.filter(status__in=[3,4]).filter(created__gt=(timezone.now() - datetime.timedelta(days=1))).filter(category=category).order_by('-created')
    
class MmaRSS(Feed):
    try:
        title = Seo.objects.get(tag=1)
    except:
        title = None

    link = "/"

    def items(self):
        category = get_object_or_404(Category, slug='mma')
        return News.objects.filter(status__in=[3,4]).filter(created__gt=(timezone.now() - datetime.timedelta(days=1))).filter(category=category).order_by('-created')

class BoksRSS(Feed):
    try:
        title = Seo.objects.get(tag=1)
    except:
        title = None

    link = "/"

    def items(self):
        category = get_object_or_404(Category, slug='boks')
        return News.objects.filter(status__in=[3,4]).filter(created__gt=(timezone.now() - datetime.timedelta(days=1))).filter(category=category).order_by('-created')
