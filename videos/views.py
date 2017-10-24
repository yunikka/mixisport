from django.shortcuts import render
from .models import Video

from lib.custom import pagination_page
from piece.utils import SeoTags

def video_list(request, template='video_list.html',):

    video_list = pagination_page(request, Video.objects.all(), 10)

    context = {
        'video_list': video_list,
        'title' : SeoTags.title(),
    }
    return render(request, template, context)