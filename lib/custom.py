from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_age(birthday):
    today = date.today()
    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day < birthday.day:
        age -= 1
    return age

def pagination_page(request, _object, lines_count):
    '''Вспомогательная функция для реализации пагинации'''
    paginator = Paginator(_object, lines_count)
    page = request.GET.get('page')
    try:
        _object = paginator.page(page)
    except PageNotAnInteger:
        _object = paginator.page(1)
    except EmptyPage:
        _object = paginator.page(paginator.num_pages)
    return _object
