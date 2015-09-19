import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from redactor.fields import RedactorField
from lib.fields import ResizeImageField

from regions.models import Country


class Fighters(models.Model):
    fullname = models.CharField(max_length=40, verbose_name="Полное имя", help_text="Введите полное имя бойца (не более 40 символов)")
    slug = models.SlugField(verbose_name="Путь", help_text="Путь - уникальное имя страницы, которое будет присутствовать в адресной строке")
    photo = ResizeImageField(upload_to='img/fighters', thumb_width=316, thumb_height=316, verbose_name="Фото", help_text="Размер изображения будет изменен на 316х316, желательно предварительно кадрировать в виде квадрата")
    country = models.ForeignKey(Country, verbose_name="Страна", help_text="Выберите Страну из списка")
    birthdate = models.DateField(verbose_name="Дата рождения", help_text="Укажите дату рождения бойца")
    height = models.IntegerField(verbose_name="Рост", help_text="Укажите рост бойца в интервале 70-299 см", validators=[RegexValidator(regex='^(([7-9][0-9])|[1-2][0-9][0-9])$',message='Неверное значение! Укажите рост бойца в интервале 70-299 см',code='invalid'),])
    weight = models.IntegerField(verbose_name="Вес", help_text="Укажите вес бойца в интервале 30-299 кг", validators=[RegexValidator(regex='^(([3-9][0-9])|[1-2][0-9][0-9])$',message='Неверное значение! Укажите вес бойца в интервале 30-299 кг',code='invalid'),])
    record = models.CharField(max_length=11, verbose_name="Рекорд", help_text="Укажите рекорд в формате ХХХ-ХХХ, например 32-1, не более 11 символов", validators=[RegexValidator(regex='^[0-9]+\-[0-9]+$',message='Неверное значение, Укажите в формате ХХХ-ХХХ, например 32-1',code='invalid'),])
    add_info = RedactorField(blank=True, verbose_name="Дополнительно", help_text="Можно ввести произвольный текст или оставить поле пустым")

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Бойцы"
        verbose_name = "Боец"
        
    def __str__(self):
        return self.fullname
    
    @permalink
    def get_absolute_url(self):
        return ('fighters', (), {'slug': self.slug})
    
    
class Events(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Введите название события (не более 100 символов)")
    slug = models.SlugField(verbose_name="Путь", help_text="Путь - уникальное имя страницы, которое будет присутствовать в адресной строке")
    location = models.CharField(max_length=100, verbose_name="Место", help_text="Укажите место проведения события")
    start_time = models.DateTimeField(default=datetime.datetime.now, verbose_name="Начало", help_text="Укажите дату/время начала события")
    visibility =  models.BooleanField(default=0, verbose_name="Видимость", help_text="Если стоит галочка, то событие отображается в общем списке")

    class Meta:
        ordering = ['-id']
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
    vote_1 = models.IntegerField(default=0, verbose_name="Количество голосов за первого бойца", editable=False)
    vote_2 = models.IntegerField(default=0, verbose_name="Количество голосов за второго бойца", editable=False)
    betting_odds_1 = models.DecimalField(default=0.00, verbose_name="Коэффцицент", help_text="Букмекерский коэффцицент для бойца №1", max_digits=5, decimal_places=2)
    betting_odds_2 = models.DecimalField(default=0.00, verbose_name="Коэффцицент", help_text="Букмекерский коэффцицент для бойца №2", max_digits=5, decimal_places=2)   
    country_1 = models.ForeignKey(Country, verbose_name="Страна ", help_text="Выберите Страну из списка для бойца №1", related_name="country_1")
    country_2 = models.ForeignKey(Country, verbose_name="Страна", help_text="Выберите Страну из списка для бойца №2", related_name="country_2")
    age_1 = models.IntegerField(default=0, verbose_name="Возраст", help_text="Введите возраст бойца №1")
    age_2 = models.IntegerField(default=0, verbose_name="Возраст", help_text="Введите возраст бойца №2")
    height_1 = models.IntegerField(verbose_name="Рост", help_text="Укажите рост бойца №1 в интервале 70-299 см", validators=[RegexValidator(regex='^(([7-9][0-9])|[1-2][0-9][0-9])$',message='Неверное значение! Укажите рост бойца в интервале 70-299 см',code='invalid'),])
    height_2 = models.IntegerField(verbose_name="Рост", help_text="Укажите рост бойца №2 в интервале 70-299 см", validators=[RegexValidator(regex='^(([7-9][0-9])|[1-2][0-9][0-9])$',message='Неверное значение! Укажите рост бойца в интервале 70-299 см',code='invalid'),])
    weight_1 = models.IntegerField(verbose_name="Вес", help_text="Укажите вес бойца №1 в интервале 30-299 кг", validators=[RegexValidator(regex='^(([3-9][0-9])|[1-2][0-9][0-9])$',message='Неверное значение! Укажите вес бойца в интервале 30-299 кг',code='invalid'),])
    weight_2 = models.IntegerField(verbose_name="Вес", help_text="Укажите вес бойца №2 в интервале 30-299 кг", validators=[RegexValidator(regex='^(([3-9][0-9])|[1-2][0-9][0-9])$',message='Неверное значение! Укажите вес бойца в интервале 30-299 кг',code='invalid'),])
    record_1 = models.CharField(max_length=11, verbose_name="Рекорд", help_text="Укажите рекорд бойца №1 в формате ХХХ-ХХХ, например 32-1, не более 11 символов", validators=[RegexValidator(regex='^[0-9]+\-[0-9]+$',message='Неверное значение, Укажите в формате ХХХ-ХХХ, например 32-1',code='invalid'),])
    record_2 = models.CharField(max_length=11, verbose_name="Рекорд", help_text="Укажите рекорд бойца №2 в формате ХХХ-ХХХ, например 32-1, не более 11 символов", validators=[RegexValidator(regex='^[0-9]+\-[0-9]+$',message='Неверное значение, Укажите в формате ХХХ-ХХХ, например 32-1',code='invalid'),])   
    events = models.ForeignKey(Events, verbose_name="Событие", help_text="Укажите событие к котору относится данная пара")
    in_mainpage = models.BooleanField(default=0, verbose_name="На главной?", help_text="Отображать данное событие на главной странице. Если отметить несколько событий, то будет отображать")
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Пары бойцов"
        verbose_name = "Пара бойцов"
        