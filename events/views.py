from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import Fighters, Events, EventPair, Statistics, Battles
from piece.utils import SeoTags
from lib.custom import pagination_page


def fighters(request, slug, template='fighters.html'):
    """По заданному ключу категории отображает все элементы этой категории."""
    fighter = get_object_or_404(Fighters, slug=slug)
    context = {
        'fighter': fighter,
        'stats': Statistics.objects.filter(fighters=fighter.id),
        'battles' : Battles.objects.filter(fighters=fighter.id),
    }
    return render(request, template, context)

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
    return render(request, template, context)

def event_list(request, template='event_list.html',):

    if 'archive' in request.path:
        archive = 1
    else:
        archive = 0

    event_list = pagination_page(request, Events.objects.filter(archive=archive), 10)

    context = {
        'event_list': event_list,
        'title' : SeoTags.title(),
        'archive' : archive,
    }
    return render(request, template, context)

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

def statistics(request, id, template='statistics.html'):
    stat = get_object_or_404(EventPair, id=id)
    event_id = stat.events.id
    context = {
        'stat': stat,
        'pairs': EventPair.objects.exclude(id__exact=id).filter(events=event_id).order_by('weight'),
        'fighters_stat': zip(Statistics.objects.filter(fighters=stat.fighters_1).exclude(type=1), Statistics.objects.filter(fighters=stat.fighters_2).exclude(type=1)),
    }
    return render(request, template, context)
