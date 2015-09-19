from django import template
from piece.models import Slider, SliderItem
from mixisport.settings import MEDIA_URL

register = template.Library() 

@register.inclusion_tag("slider.html")
def show_slider():
    enable_slider = Slider.objects.filter(enable=1).order_by('pk')
    slideritem = SliderItem.objects.filter(slider__in=list(enable_slider)).filter(enable=1).order_by('pk')
    firstslide = slideritem[0]
    lastslide = slideritem.reverse()[0]
    middleslide = slideritem.exclude(id__in=[firstslide.id,lastslide.id]).order_by('pk')
    steps = [x for x in range(1, len(slideritem))]
    return {'firstslide': firstslide, 'lastslide': lastslide, 'middleslide': middleslide, 'steps': steps, 'MEDIA_URL': MEDIA_URL}