from django import template
from piece.models import Seo

register = template.Library() 

@register.inclusion_tag("seo_tags.html")
def show_seotags():
    context = {
        'description': Seo.objects.get(tag=2),
        'keywords': Seo.objects.get(tag=3),
    }
    return context