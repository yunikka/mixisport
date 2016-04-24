from django import template
from piece.models import Slider, SliderItem
from mixisport.settings import MEDIA_URL

register = template.Library() 

@register.inclusion_tag("slider.html")
def show_slider():
    enable_slider = Slider.objects.filter(enable=1).order_by('pk')
    slideritems = SliderItem.objects.filter(slider__in=list(enable_slider)).filter(enable=1).order_by('pk')
    return {'slideritems': slideritems, 'MEDIA_URL': MEDIA_URL}