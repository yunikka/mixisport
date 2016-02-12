from django import template
from piece.models import Commerce

register = template.Library() 

@register.inclusion_tag("tags_informer_left.html")
def show_informer_left():
    context = {
        'code': Commerce.objects.get(code_type=0),
    }
    return context