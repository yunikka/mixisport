from django import template
from photologue.models import Gallery
from mixisport.settings import MEDIA_URL

register = template.Library() 

@register.inclusion_tag("gallery_tags.html")
def show_gallery_tags():
    galleries = Gallery.objects.all()[0:3]
    return {'galleries': galleries, 'MEDIA_URL': MEDIA_URL}