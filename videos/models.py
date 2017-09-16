from django.db import models
from news.models import Category

import datetime

class Video(models.Model):

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Путь", unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория")
    content = models.TextField(verbose_name="Видео контент")
    created = models.DateTimeField(default=datetime.datetime.now, verbose_name="Создано")

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.title