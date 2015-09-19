from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from .models import Pages

def PagesView(request, slug, template='pages.html'):
    # Выбираем заголовки
    title = get_object_or_404(Pages, slug=slug)
    context = {
        'pages': Pages.objects.get(title=title)
    }
    return render_to_response(template, context, RequestContext(request))