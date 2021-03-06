from django.conf.urls import *
from django.views.generic import ListView
from .models import News
from .views import StoryDetailView, StoryListView, category, contact
from .rss.feeds import DefaultRSS, SocialRSS, RSS_limit_content, BodibildingRSS, MmaRSS, BoksRSS
from .rss.yandex import YandexRSS


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', StoryDetailView.as_view(), name="news"),
    url(r'^$', StoryListView),
    url(r'^category/(?P<slug>[-\w]+)/$', category, name="news-category"),
    url(r'^contact$', contact, name="contact"),
    url(r'^rss.xml$', DefaultRSS()),
    url(r'^rss/yandex.xml$', YandexRSS()),
    url(r'^rss/social.xml$', SocialRSS()),
    url(r'^rss/limit.xml$', RSS_limit_content()),
    url(r'^category/bodibilding/rss.xml$', BodibildingRSS()),
    url(r'^category/mma/rss.xml$', MmaRSS()),
    url(r'^category/boks/rss.xml$', BoksRSS()),    
]