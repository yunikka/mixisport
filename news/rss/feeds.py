from django.contrib.syndication.views import Feed
from news.models import News

class LastNews(Feed):
    title = "MIXISport - Новости силовых видов спорта"
    link = "/"

    def items(self):
#        return News.objects.all()
        return News.objects.filter(status__in=[3,4]).order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content