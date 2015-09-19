from django import template
from pages.models import Pages

register = template.Library() 

@register.inclusion_tag("pages_list.html")
def show_pages():
    context = {
        'pages': Pages.objects.filter(enable=1),
    }
    return context