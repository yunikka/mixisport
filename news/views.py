from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import DetailView
from lib.custom import pagination_page
from .models import News, Category
from piece.models import Seo
from .forms import NameForm

from piece.utils import SeoTags


def StoryListView(request, template='index.html'):

    news_list = pagination_page(request, News.objects.filter(status__in=[3,4]), 10)

    context = {
        'news_list': news_list,
        'title' : SeoTags.title()
    }
    return render(request, template, context)


class StoryDetailView(DetailView):
    model = News
    template_name = "article.html"

def category(request, slug, template='index.html', page_template='index_page.html'):
    """По заданному ключу категории отображает все элементы этой категории."""
    category = get_object_or_404(Category, slug=slug)
    context = {
        'news_list': News.objects.filter(status__in=[3,4]).filter(category=category),
        'page_template': page_template,
        'title' : Seo.objects.get(tag=1),
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(template, context, RequestContext(request))

def contact(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            request.session["name"] = request.POST.get('your_name')
            form = NameForm()

    else:
        form = NameForm()
        
    if "name" not in request.session:
        request.session["name"] = 'Не выбрано'
    else:
        pass
    
    # Ищем статьи по заданному критерию, если такого нет, то просто присваиваем значение по умолчанию
#    try:
#        a = News.objects.filter(status__in=[3,4]).filter(category=Category.objects.get(label=request.session["name"]).id)
#    except:
#        a = ['Нет такого']
    
    context = {
        'form': form,
        'session_name': Category.objects.get(id=request.session["name"]),
        'news_list': News.objects.filter(status__in=[3,4]).filter(category=request.session["name"])
    }
    
         
    return render(request, 'contact.html', context)