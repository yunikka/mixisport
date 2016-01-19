from django.conf.urls import *
from django.views.generic import ListView
from .models import News
from .views import StoryDetailView, StoryListView, category, contact
from .rss.feeds import DefaultRSS, SocialRSS, RSS_limit_content
from .rss.yandex import YandexRSS


urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$', StoryDetailView.as_view(), name="news"),
    url(r'^$', StoryListView),
)

urlpatterns += patterns('.views',
    url(r'^category/(?P<slug>[-\w]+)/$', category, name="news-category"),
    url(r'^contact$', contact, name="contact"),
    url(r'^rss.xml$', DefaultRSS()),
    url(r'^rss/yandex.xml$', YandexRSS()),
    url(r'^rss/social.xml$', SocialRSS()),
    url(r'^rss/limit.xml$', RSS_limit_content()),
)
