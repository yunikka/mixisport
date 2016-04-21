from django.conf.urls import *
from .views import fighters, events, event_list, pair_vote, statistics

urlpatterns = patterns('.views',
    url(r'^fighters/(?P<slug>[-\w]+)/$', fighters, name="fighters"),
    url(r'^archive/$', event_list, name="event_list_archive"),
    url(r'^vote/(?P<id>[0-9]+)/(?P<vote>[1-2]+)/$', pair_vote, name="pair_vote"),
    url(r'^statistics/(?P<id>[0-9]+)/$', statistics, name="statistics"),
    url(r'(?P<slug>[-\w]+)/$', events, name="events"),
    url(r'^$', event_list, name="event_list"),
)