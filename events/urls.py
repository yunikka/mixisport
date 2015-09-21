from django.conf.urls import *
from .views import fighters, events, event_list

urlpatterns = patterns('.views',
    url(r'^fighters/(?P<slug>[-\w]+)/$', fighters, name="fighters"),
    url(r'(?P<slug>[-\w]+)/$', events, name="events"),
    url(r'^$', event_list, name="event_list"),
)