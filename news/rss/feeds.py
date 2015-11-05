from django.contrib.syndication.views import Feed
from news.models import News

class LastNews(Feed):
    title = "MIXISport - Новости силовых видов спорта"
    link = "/"

    def items(self):
        return News.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content