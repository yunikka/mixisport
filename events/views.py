from django.shortcuts import render_to_response, get_object_or_404, redirect
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
    
    session_flag = [] # Генерируем флаги сессий
    for x in EventPair.objects.filter(events=event.id): # проверяем наличие сессий для кажого голосования
        if "vote_pair_%s" % x.id not in request.session: # проверяем наличие сессионного ключа для данной пары
            request.session["vote_pair_%s" % x.id] = 0
        else:
            pass
        session_flag.append(request.session["vote_pair_%s" % x.id]) # последовательно добавляем флаги
    
        
        
    context = {
        'event': Events.objects.get(id=event.id),
        'pairs': EventPair.objects.filter(events=event.id).order_by('weight'),
        'session_flag': session_flag,
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
    # Ссылка для голосования
    # Проверяем не голосовал ли уже
    if "vote_pair_%s" % id not in request.session:
        request.session["vote_pair_%s" % id] = 0
    elif request.session["vote_pair_%s" % id] == 1: # запрещает голосовать вызывая 404
        raise Http404("Страница не существует") 
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
    
    return_path  = request.META.get('HTTP_REFERER','/')
    return redirect(return_path)