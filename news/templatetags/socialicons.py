from django import template
from piece.models import SocialIcons

register = template.Library() 

@register.inclusion_tag("socialicons.html")
def show_socialicons():
    context = {
        'socialicons': SocialIcons.objects.all(),
    }
    return context