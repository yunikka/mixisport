from django.db import models
from lib.fields import ResizeImageField

class Slider(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя баннера", help_text="Не более 30 символов")
    enable = models.BooleanField(verbose_name="Включить?")

    class Meta:
        verbose_name_plural = "Слайдеры"

    def __str__(self):
        return self.name

class SliderItem(models.Model):
    slider = models.ForeignKey(Slider)
    title = models.CharField(max_length=30, verbose_name="Имя фото", help_text="Не более 30 символов")
    text = models.CharField(max_length=100, verbose_name="Текст", help_text="Не более 100 символов")
    button = models.CharField(max_length=30, verbose_name="Текст кнопки",  help_text="Не более 30 символов")
    url_button = models.URLField(verbose_name="Ссылка", help_text="Не более 200 символов")
    image = ResizeImageField(upload_to='img/slider_images', verbose_name="Изображение 1140х475", help_text="Размер изображения в пропорции 1140х475",thumb_width=1140, thumb_height=475)
    enable = models.BooleanField(verbose_name="Включен?")

    class Meta:
        verbose_name_plural = "Элементы слайлера"
    
    def __str__(self):
        return self.title
    
class Ticker(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя", help_text="Не более 20 символов, нигде не отоброжается")
    text = models.TextField(max_length=300, verbose_name="Текст", help_text="Не более 300 символов")
    enable = models.BooleanField(verbose_name="Включить?")
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Бегущая строка"
        
    def __str__(self):
        return self.name
    
class Seo(models.Model):
    TAG_CHOICES = (
        (1, "title"),
        (2, "description"),
        (3, "keywords"),
    )
    tag = models.IntegerField(choices=TAG_CHOICES, default=1, unique=True, verbose_name="Тег", help_text="Не более 40 символов")
    code = models.CharField(max_length=255, verbose_name="Код", help_text="Не более 300 символов")
    
    class Meta:
        ordering = ['tag']
        verbose_name_plural = "Настройки SEO-тегов"
        verbose_name = "SEO-тег"
        
    def __str__(self):
        return self.code
    
class SocialIcons(models.Model):
    name = models.CharField(max_length=40, verbose_name="Имя", help_text="Не более 20 символов")
    url = models.URLField(verbose_name="Ссылка", help_text="Не более 200 символов")
    icon_code = models.CharField(max_length=20, verbose_name="Код pictonic", help_text="Код иконки можно посмотреть на https://pictonic.co/free")
    weight = models.IntegerField(default=5, verbose_name="Сортировка", help_text="Чем меньше значение, тем первее будет отображена")
    
    class Meta:
        ordering = ['weight']
        verbose_name_plural = "Иконки соцсетей"
        verbose_name = "Иконка соцсети"
        
    def __str__(self):
        return self.name
