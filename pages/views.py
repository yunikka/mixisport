from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .models import Pages

def PagesView(request, slug, template='pages.html'):
    # Выбираем заголовки
    title = get_object_or_404(Pages, slug=slug)
    context = {
        'pages': Pages.objects.get(title=title)
    }
    return render(request, template, context)