from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
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
    if 'archive' in request.path:
        archive = 1
    else:
        archive = 0
    context = {
        'event_list': Events.objects.filter(archive=archive),
        'page_template': page_template,
        'title' : Seo.objects.get(tag=1),
        'archive' : archive,
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(template, context, RequestContext(request))

def pair_vote(request, id, vote):
    
    # Проверяем не голосовал ли уже
    if "vote_pair_%s" % id not in request.session:
        request.session["vote_pair_%s" % id] = 0
    elif request.session["vote_pair_%s" % id] == 1:
        raise Http404("за %s уже голосовал" % id)
    else:
        pass
    
    # Получаем объект пары бойцов и в зависимости от vote увеличиваем значение
    pair = get_object_or_404(EventPair, id=id)
    if vote == '1':
        pair.vote_1 += 1
    elif vote == '2':
        pair.vote_2 += 1
    else:
        raise Http404()
    request.session["vote_pair_%s" % id] = 1
    pair.save()
    
    if 'HTTP_REFERER' in request.META :
        referer = request.META['HTTP_REFERER']
    else:
        referer = ''
    
    return referer



