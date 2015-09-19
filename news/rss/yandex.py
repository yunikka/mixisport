from django.contrib.syndication.views import Feed
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.feedgenerator import Rss201rev2Feed

from news.models import News

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
    
    def add_item_elements(self, handler, item):
        if item['description'] is not None:
            handler.addQuickElementCDATA(u'description', item['description'])
            item['description'] = None
        super(Rss, self).add_item_elements(handler, item)


class RssYandex(Rss):
    def rss_attributes(self):
        attrs = super(RssYandex, self).rss_attributes()
        attrs.update({'xmlns':'http://backend.userland.com/rss2', 'xmlns:yandex':'http://news.yandex.ru'})
        return attrs
    
    def add_item_elements(self, handler, item):
        if item['fulltext'] is not None:
            handler.addQuickElementCDATA(u'yandex:full-text', item['fulltext'])
        super(RssYandex, self).add_item_elements(handler, item)
        
class MyFeed(Feed):
    feed_type = RssYandex

    def item_extra_kwargs(self, item):
        return {'fulltext':item.body.rendered}