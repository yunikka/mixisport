from django.conf.urls import *
from .views import PagesView

urlpatterns = patterns('',
    url(r'^(?P<slug>[-\w]+)/$', PagesView, name="pages"),
)
