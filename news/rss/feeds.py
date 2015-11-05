from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from news.models import News
from piece.models import Seo

class YandexFeedGenerator(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(YandexFeedGenerator, self).add_item_elements(handler, item)
        # Добавление кастомного тега в RSS-ленту
        handler.addQuickElement(u"yandex:full-text", item["content"])

class DefaultRSS(Feed):
    title = Seo.objects.get(tag=1)
    description = Seo.objects.get(tag=2)
    link = "/"

    def items(self):
        return News.objects.filter(status__in=[3,4]).order_by('-created')[:30]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        return item.content
    
class YandexRSS(Feed):
    feed_type = YandexFeedGenerator  
    title = Seo.objects.get(tag=1)
    description = Seo.objects.get(tag=2)
    link = "/"
    
    def items(self):
        return News.objects.filter(status__in=[3,4]).order_by('-created')[:30]

    def item_title(self, item):
        return item.title
        
    def item_pubdate(self, item):
        return item.created

    def item_extra_kwargs(self, item):
        return {
            "content": item.content,
        }