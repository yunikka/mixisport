from django import template
from news.models import Category

register = template.Library() 

@register.inclusion_tag("cat_menu.html")
def show_catmenu():
    categories = Category.objects.all().order_by("label")
    return {'categories': categories}