from django import template
from piece.models import Ticker

register = template.Library() 

@register.inclusion_tag("ticker.html")
def show_ticker():
    tickers = Ticker.objects.filter(enable=1).order_by('-pk')
    return {'tickers': tickers}