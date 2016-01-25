from django.contrib.syndication.views import Feed
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.feedgenerator import Rss201rev2Feed

import re
from django.utils import timezone
import datetime

from news.models import News
from piece.models import Seo


class SXG(SimplerXMLGenerator):
    def addQuickElementCDATA(self, name, contents=None, attrs=None):
        if attrs is None: attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            self._write('<![CDATA['+contents+']]>')
        self.endElement(name)
        

class Rss(Rss201rev2Feed):
    def write(self, outfile, encoding):
        handler = SXG(outfile, encoding)
        handler.startDocument()
        handler.startElement(u"rss", self.rss_attributes())
        handler.startElement(u"channel", self.root_attributes())
        self.add_root_elements(handler)
        self.write_items(handler)
        self.endChannelElement(handler)
        handler.endElement(u"rss")
        
    def add_root_elements(self, handler):
        super(Rss, self).add_root_elements(handler)
        handler.addQuickElement(u'yandex:logo', 'http://mixisport.com/media/img/rss/logo100.png',)     
        handler.addQuickElement(u'yandex:logo', 'http://mixisport.com/media/img/rss/logo180.png', {'type': 'square'})     

class RssYandex(Rss):
    def rss_attributes(self):
        attrs = super(RssYandex, self).rss_attributes()
        attrs.update({'xmlns:yandex':'http://news.yandex.ru', 'xmlns:media':'http://search.yahoo.com/mrss/'})
        return attrs
    
    def add_item_elements(self, handler, item):
        if item['description'] is not None:
            handler.addQuickElement(u'yandex:full-text', item['description'])
        super(RssYandex, self).add_item_elements(handler, item)
        
class YandexRSS(Feed):
    feed_type = RssYandex
    title = Seo.objects.get(tag=1)
    description = Seo.objects.get(tag=2)
    
    link = "/"
    
    def items(self):
        return News.objects.filter(status__in=[3,4]).filter(created__gt=(timezone.now() - datetime.timedelta(days=7))).order_by('-created')

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