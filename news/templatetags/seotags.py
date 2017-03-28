from django import template
from piece.utils import SeoTags

register = template.Library() 

@register.inclusion_tag("seo_tags.html")
def show_seotags():
    context = {
        'description': SeoTags.description(),
        'keywords': SeoTags.keywords(),
    }
    return context