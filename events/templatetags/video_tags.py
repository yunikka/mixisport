from django import template
from videos.models import Video

register = template.Library() 

@register.inclusion_tag("video_tags.html")
def show_video_tags():
    videos = Video.objects.all()[0:3]
    return {'videos': videos,}