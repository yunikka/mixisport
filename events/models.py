import datetime, math
from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from redactor.fields import RedactorField
from lib.fields import ResizeImageField
from stdimage.models import StdImageField

from regions.models import Country


class Fighters(models.Model):
    fullname = models.CharField(max_length=40, verbose_name="Полное имя", help_text="Введите полное имя бойца (не более 40 символов)")
    slug = models.SlugField(verbose_name="Путь", help_text="Путь - уникальное имя страницы, которое будет присутствовать в адресной строке")
    photo = ResizeImageField(upload_to='img/fighters', thumb_width=316, thumb_height=316, verbose_name="Фото в разделе ИНФО", help_text="Размер изображения будет изменен на 316х316, желательно предварительно кадрировать в виде квадрата")
    photo_left = models.ImageField(upload_to='img/fighters_left', default=None, verbose_name="Фото слева", help_text="Размер изображения будет растянуто. Рекомендуется вертикальное позиционирование", blank=True)
    country = models.ForeignKey(Country, verbose_name="Страна", help_text="Выберите Страну из списка")
    birthdate = models.DateField(verbose_name="Дата рождения", help_text="Укажите дату рождения бойца")
    height = models.DecimalField(default=0.00, verbose_name="Рост", help_text="Укажите рост бойца №1", max_digits=5, decimal_places=2)
    weight = models.DecimalField(default=0.00, verbose_name="Вес", help_text="Укажите вес бойца №2", max_digits=5, decimal_places=2)
    record = models.CharField(max_length=11, verbose_name="Рекорд", help_text="Укажите значение Рекорд")
    biography = RedactorField(blank=True, verbose_name="Биография", help_text="Можно ввести произвольный текст или оставить поле пустым")

    class Meta:
        ordering = ['fullname']
        verbose_name_plural = "Бойцы"
        verbose_name = "Боец"
        
    def __str__(self):
        return self.fullname
    
    @permalink
    def get_absolute_url(self):
        return ('fighters', (), {'slug': self.slug})

    def get_age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if today.month < self.birthdate.month:
            age -= 1
        elif today.month == self.birthdate.month and today.day < self.birthdate.day:
            age -= 1
        return age
    
class Statistics(models.Model):
    STATS_TYPE = (
        (1, "Всего"),
        (2, "Нокаут"),
        (3, "Сабмишин"),
        (4, "Решением"),
    )
    fighters = models.ForeignKey(Fighters, verbose_name="Имя бойца")
    type = models.IntegerField(choices=STATS_TYPE, default=1, verbose_name="Тип")
    victory = models.IntegerField(default=0, verbose_name="Побед")
    defeat = models.IntegerField(default=0, verbose_name="Поражений")

    def __str__(self):
        return self.get_type_display()

    class Meta:
        unique_together = ('fighters', 'type',)
        ordering = ['type']
        verbose_name_plural = "Статистика"
        verbose_name = "Статистика"
        
    def proc_victory(self): # функция вычисляет проценты от количества побед
        if self.victory > 0 and self.defeat == 0:
            res = 100
        elif self.victory == 0 and self.defeat == 0:
            res = 0
        else:
            res = (self.victory*100)/(self.victory+self.defeat)
        return round(res)
    
    def proc_defeat(self): # функция вычисляет проценты от количества поражений
        if self.defeat > 0 and self.victory == 0:
            res = 100
        elif self.defeat == 0 and self.victory == 0:
            res = 0
        else:
            res = (self.defeat*100)/(self.defeat+self.victory)
        return round(res)    
    
class Events(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Введите название события (не более 100 символов)")
    slug = models.SlugField(verbose_name="Путь", unique=True, help_text="Путь - уникальное имя страницы, которое будет присутствовать в адресной строке")
    location = models.CharField(max_length=100, verbose_name="Место", help_text="Укажите место проведения события")
    start_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="Начало", help_text="Укажите дату/время начала события")
    archive =  models.BooleanField(default=0, verbose_name="Архив", help_text="Если стоит галочка, то событие уходит в архив")
    image_up = models.ImageField(blank=True, upload_to='img/image_events', verbose_name="Картинка события",)
    image_thumbnail = StdImageField(blank=True, variations={'thumbnail': {'width': 160,}}, upload_to='img/image_events/thumbnail', verbose_name="Миниатюра для заголовка")

    class Meta:
        ordering = ['-start_time']
        verbose_name_plural = "События"
        verbose_name = "Событие"
        
    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('events', (), {'slug': self.slug})

    
class EventPair(models.Model):
    fighters_1 = models.ForeignKey(Fighters, verbose_name="Боец №1", help_text="Выберите бойца из списка или заведите нового", related_name="first_fighter")
    fighters_2 = models.ForeignKey(Fighters, verbose_name="Боец №2", help_text="Выберите бойца из списка или заведите нового", related_name="second_fighter")
    vote_1 = models.IntegerField(default=0, verbose_name="Голоса", help_text="Количество голосов за бойца №1")
    vote_2 = models.IntegerField(default=0, verbose_name="Голоса", help_text="Количество голосов за бойца №2")
    defeat_1 = models.BooleanField(default=0, verbose_name="Поражение бойца 1?", help_text="Означает что данный боец потерпел поражение")
    defeat_2 = models.BooleanField(default=0, verbose_name="Поражение бойца 2?", help_text="Означает что данный боец потерпел поражение")
    betting_odds_1 = models.DecimalField(default=0.00, verbose_name="Коэффцицент", help_text="Букмекерский коэффцицент для бойца №1", max_digits=5, decimal_places=2)
    betting_odds_2 = models.DecimalField(default=0.00, verbose_name="Коэффцицент", help_text="Букмекерский коэффцицент для бойца №2", max_digits=5, decimal_places=2)   
    punches_head_1 = models.IntegerField(default=0, verbose_name="Удары руками в голову")
    punches_body_1 = models.IntegerField(default=0, verbose_name="Удары руками в корпус")
    kicks_head_1 = models.IntegerField(default=0, verbose_name="Удары ногами в голову")
    kicks_body_1 = models.IntegerField(default=0, verbose_name="Удары ногами в корпус")
    throws_1 = models.IntegerField(default=0, verbose_name="Броски")
    punches_head_2 = models.IntegerField(default=0, verbose_name="Удары руками в голову")
    punches_body_2 = models.IntegerField(default=0, verbose_name="Удары руками в корпус")
    kicks_head_2 = models.IntegerField(default=0, verbose_name="Удары ногами в голову")
    kicks_body_2 = models.IntegerField(default=0, verbose_name="Удары ногами в корпус")
    throws_2 = models.IntegerField(default=0, verbose_name="Броски")
    content_stats = RedactorField(blank=True, verbose_name="Произвольный контент")
    enable_stats = models.BooleanField(default=0, verbose_name="Включить отображение статистики?")
    events = models.ForeignKey(Events, verbose_name="Событие", help_text="Укажите событие к котору относится данная пара")
    in_mainpage = models.BooleanField(default=0, verbose_name="На главной?", help_text="Отображать данное событие на главной странице. Если отметить несколько событий, то будет отображать")
    weight = models.IntegerField(default=0, verbose_name="Значимость", help_text="Чем больше значение, тем выше будет отображена пара")
    
    class Meta:
        ordering = ["events__name"]

    def proc_vote_1(self): # функция вычисляет проценты голосова для первого бойца
        if self.vote_1 > 0 and self.vote_2 == 0:
            res = 100
        elif self.vote_1 == 0 and self.vote_2 == 0:
            res = 0
        else:
            res = (self.vote_1*100)/(self.vote_1+self.vote_2)
        return round(res)
    
    def proc_vote_2(self): # функция вычисляет проценты голосова для второго бойца
        if self.vote_2 > 0 and self.vote_1 == 0:
            res = 100
        elif self.vote_2 == 0 and self.vote_1 == 0:
            res = 0
        else:
            res = (self.vote_2*100)/(self.vote_2+self.vote_1)
        return round(res)
    
    def already_vote(request, self): # флаг который сообщает, что уже голосовали
        if "vote_pair_%s" % self.id not in request.session: # проверяем наличие сессионного ключа для данной пары
            request.session["vote_pair_%s" % self.id] = 0
        else:
            pass
        return request.session["vote_pair_%s" % self.id]
    
    def __str__(self):
        result = self.events.name + ': ' + self.fighters_1.fullname + ' VS ' + self.fighters_2.fullname
        return result

    
class EventPair_Statistics(models.Model):
    punches_head_1 = models.IntegerField(default=0, verbose_name="Удары руками в голову")
    punches_body_1 = models.IntegerField(default=0, verbose_name="Удары руками в корпус")
    kicks_head_1 = models.IntegerField(default=0, verbose_name="Удары ногами в голову")
    kicks_body_1 = models.IntegerField(default=0, verbose_name="Удары ногами в корпус")
    throws_1 = models.IntegerField(default=0, verbose_name="Броски")
    punches_head_2 = models.IntegerField(default=0, verbose_name="Удары руками в голову")
    punches_body_2 = models.IntegerField(default=0, verbose_name="Удары руками в корпус")
    kicks_head_2 = models.IntegerField(default=0, verbose_name="Удары ногами в голову")
    kicks_body_2 = models.IntegerField(default=0, verbose_name="Удары ногами в корпус")
    throws_2 = models.IntegerField(default=0, verbose_name="Броски")

class Battles(models.Model):

    fighters = models.ForeignKey(Fighters, verbose_name="Имя бойца")
    eventpair = models.ForeignKey(EventPair, verbose_name="Пара бойцов")

    class Meta:
        verbose_name_plural = "Бои"
        verbose_name = "Бой"
