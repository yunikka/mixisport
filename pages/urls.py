from django.conf.urls import *
from .views import PagesView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', PagesView, name="pages"),
]
