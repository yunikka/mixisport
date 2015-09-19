from django.conf.urls import *
from django.views.generic import ListView
from .models import News
from .views import StoryDetailView, StoryListView, category, contact
from .rss.yandex import MyFeed


urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$', StoryDetailView.as_view(), name="news"),
    url(r'^$', StoryListView),
)

urlpatterns += patterns('.views',
    url(r'^category/(?P<slug>[-\w]+)/$', category, name="news-category"),
    url(r'^contact$', contact, name="contact"),
    url(r'^rss/yandex$', MyFeed()),
)
