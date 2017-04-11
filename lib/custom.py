from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from events.models import Statistics

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


class FightersStat(object):
    '''Получаем данные о бойце и выводим его статистику'''

    def __init__(self, fighter_id):
        self.stats = Statistics.objects.filter(fighters=fighter_id).exclude(type=1)

    def total_victory(self):
        '''Функция подсчета всех побед'''
        total_victory = 0
        for stat in self.stats:
            total_victory += stat.victory
        return total_victory


    def total_victory_proc(self):
        '''Функция подсчета процентов побед'''
        if self.total_victory() > 0 and self.total_defeat() == 0:
            total_victory_proc = 100
        elif self.total_victory() == 0 and self.total_defeat() == 0:
            total_victory_proc = 0
        else:
            total_victory_proc = (self.total_victory()*100)/(self.total_victory()+self.total_defeat())
        return round(total_victory_proc)


    def total_defeat(self):
        '''Функция подсчета всех поражений'''
        total_defeat = 0
        for stat in self.stats:
            total_defeat += stat.defeat
        return total_defeat


    def total_defeat_proc(self):
        '''Функция подсчета процентов поражений'''
        if self.total_defeat() > 0 and self.total_defeat() == 0:
            total_defeat_proc = 100
        elif self.total_defeat() == 0 and self.total_defeat() == 0:
            total_defeat_proc = 0
        else:
            total_defeat_proc = (self.total_defeat()*100)/(self.total_victory()+self.total_defeat())
        return round(total_defeat_proc)


    def knockout_victory(self):
        '''Функция возврата побед нокаутом'''
        return self.stats.get(type=2).victory


    def knockout_defeat(self):
        '''Функция возврата поражений нокаутом'''
        return self.stats.get(type=2).defeat


    def knockout_victory_proc(self):
        '''Функция подсчета процентов побед нокаутом'''
        if self.total_victory() == 0 or self.knockout_victory() == 0:
            return 0
        else:
            return round((self.knockout_victory()*100)/self.total_victory())


    def knockout_defeat_proc(self):
        '''Функция подсчета процентов поражений нокаутом'''
        if self.total_defeat() == 0 or self.knockout_defeat() == 0:
            return 0
        else:
            return round((self.knockout_defeat()*100)/self.total_defeat())


    def submission_victory(self):
        '''Функция возврата побед сабмишеном'''
        return self.stats.get(type=3).victory


    def submission_defeat(self):
        '''Функция возврата поражений сабмишеном'''
        return self.stats.get(type=3).defeat


    def submission_victory_proc(self):
        '''Функция подсчета процентов побед сабмишеном'''
        if self.total_victory() == 0 or self.submission_victory() == 0:
            return 0
        else:
            return round((self.submission_victory()*100)/self.total_victory())


    def submission_defeat_proc(self):
        '''Функция подсчета процентов поражений сабмишеном'''
        if self.total_defeat() == 0 or self.submission_defeat() == 0:
            return 0
        else:
            return round((self.submission_defeat()*100)/self.total_defeat())


    def decision_victory(self):
        '''Функция возврата побед решением'''
        return self.stats.get(type=4).victory

    def decision_defeat(self):
        '''Функция возврата поражений решением'''
        return self.stats.get(type=4).defeat

    def decision_victory_proc(self):
        '''Функция подсчета процентов побед решением'''
        if self.total_victory() == 0 or self.decision_victory() == 0:
            return 0
        else:
            return round((self.decision_victory()*100)/self.total_victory())

    def decision_defeat_proc(self):
        '''Функция подсчета процентов поражений решением'''
        if self.total_defeat() == 0 or self.decision_defeat() == 0:
            return 0
        else:
            return round((self.decision_defeat()*100)/self.total_defeat())