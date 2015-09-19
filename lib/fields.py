from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os

#def _add_thumb(s):
#    """
#    Изменяет строку (имя файла, URL), содержащую имя файла изображения,
#    вставляя '.thumb' перед расширением имени файла
#    (которое изменяется на '.jpg').
#    """
#    parts = s.split(".")
#    parts.insert(-1, "thumb")
#    if parts[-1].lower() not in ['jpeg', 'jpg']:
#        parts[-1] = 'jpg'
#    return ".".join(parts)

class ResizeImageFieldFile(ImageFieldFile):
#    def _get_thumb_path(self):
#        return _add_thumb(self.path)
#    thumb_path = property(_get_thumb_path)

#    def _get_thumb_url(self):
#        return _add_thumb(self.url)
#    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ResizeImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)
        img.thumbnail(
            (self.field.thumb_width, self.field.thumb_height),
            Image.ANTIALIAS
        )
        img.save(self.path)

     ### Удаление крупного изображения ###
#        if os.path.exists(self.path):
#            os.remove(self.path)
#        else:
#            pass

    def delete(self, save=True):
        if os.path.exists(self.path):
            os.remove(self.path)
        super(ResizeImageFieldFile, self).delete(save)

class ResizeImageField(ImageField):
    """
    Ведет себя так же, как обычный класс ImageField, но дополнительно
    сохраняет миниатюру (JPEG) изображения и предоставляет методы
    get_FIELD_thumb_url() и get_FIELD_thumb_filename().
    Принимает два дополнительных, необязательных аргумента: thumb_width
    и thumb_height, каждый из которых имеет значение по умолчанию
    128 (пикселей). При изменении размеров отношение ширины к высоте
    сохраняется,обеспечивая пропорциональность изображения;
    за дополнительной информацией обращайтесь к описанию метода
    Image.thumbnail() в библиотеке PIL.
    """
    attr_class = ResizeImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ResizeImageField, self).__init__(*args, **kwargs)
