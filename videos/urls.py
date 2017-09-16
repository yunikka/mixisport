from django.conf.urls import *
from .views import video_list

urlpatterns = [
    url(r'^$', video_list, name="video_list"),
]