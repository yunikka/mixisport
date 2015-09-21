import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
#from tinymce.models import HTMLField
from redactor.fields import RedactorField
from smart_selects.db_fields import ChainedForeignKey 
from regions.models import MacroRegion, Region
from lib.fields import ResizeImageField


VIEWABLE_STATUS = [3, 4]

class ViewableManager(models.Manager):
    def get_queryset(self):
        default_queryset = super(ViewableManager, self).get_queryset()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)

class Category(models.Model):
    """Категория содержимого"""
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Категория"
        ordering = ['-id']

    def __str__(self):
        return self.label

class News(models.Model):
    """Элемент информационного наполнения нашего сайта,
        обычно соответствует странице"""
    STATUS_CHOICES = (
        (1, "Черновик"),
        (2, "Не согласовано"),
        (3, "Опубликовано"),
        (4, "Архив"),
    )
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Путь", unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория")
    macroregion = models.ForeignKey(MacroRegion)
    region = ChainedForeignKey(
        Region,
        chained_field='macroregion',
        chained_model_field='macroregion',
        show_all=False,
        auto_choose=True
    )
    image = ResizeImageField(upload_to='img/title_images', verbose_name="Картинка для заголовка", thumb_width=116, thumb_height=116)
#    content = HTMLField(blank=True, verbose_name="Текст статьи")
    content = RedactorField(blank=True, verbose_name="Текст статьи")
    owner = models.ForeignKey(User, verbose_name="Автор")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="Статус")
    created = models.DateTimeField(default=datetime.datetime.now, verbose_name="Создано")
    modified = models.DateTimeField(default=datetime.datetime.now, verbose_name="Изменено")

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Новости"
        
    def __str__(self):
        return self.title

    admin_objects = models.Manager()
    objects = ViewableManager()

    @permalink
    def get_absolute_url(self):
        return ('news', (), {'slug': self.slug})