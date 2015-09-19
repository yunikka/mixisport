import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
#from tinymce.models import HTMLField
from redactor.fields import RedactorField

class Pages(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Не более 100 символов")
    slug = models.SlugField(verbose_name="Путь", help_text="URL до статьи, при желании можно изменить")
#    content = HTMLField(blank=True, verbose_name="Текст статьи")
    content = RedactorField(blank=True, verbose_name="Текст статьи")
    enable = models.BooleanField(verbose_name="Включить?", help_text="Убеите галку, если не нужно отображать")
    weight = models.IntegerField(default=5, verbose_name="Сортировка", help_text="Чем меньше значение, тем первее будет отображена")
    created = models.DateTimeField(default=datetime.datetime.now, verbose_name="Создано")
    modified = models.DateTimeField(default=datetime.datetime.now, verbose_name="Изменено")

    class Meta:
        ordering = ['weight']
        verbose_name_plural = "Страницы"
        verbose_name = "Страница"
        
    def __str__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ('pages', (), {'slug': self.slug})