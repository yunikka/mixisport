from django import template
from events.models import EventPair
from mixisport.settings import MEDIA_URL

register = template.Library() 

@register.inclusion_tag("event_tags.html")
def show_event_tags():
    pairs = EventPair.objects.filter(in_mainpage=1).order_by('pk')
    return {'pairs': pairs, 'MEDIA_URL': MEDIA_URL}