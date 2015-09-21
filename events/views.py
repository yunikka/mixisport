from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .models import Fighters, Events, EventPair
from piece.models import Seo


def fighters(request, slug, template='fighters.html'):
    """По заданному ключу категории отображает все элементы этой категории."""
    context = {
        'fighter': get_object_or_404(Fighters, slug=slug),
    }
    return render_to_response(template, context, RequestContext(request))

def events(request, slug, template='events.html'):
    """Отображает события"""
    event = get_object_or_404(Events, slug=slug)
    context = {
        'event': Events.objects.get(id=event.id),
        'pairs': EventPair.objects.filter(events=event.id)
    }
    return render_to_response(template, context, RequestContext(request))

def event_list(request, template='event_list.html', page_template='event_list_page.html'):
    context = {
        'event_list': Events.objects.filter(visibility=1),
        'page_template': page_template,
        'title' : Seo.objects.get(tag=1)
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(template, context, RequestContext(request))