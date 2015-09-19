from django.db import models

class MacroRegion(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Макрорегион"
        ordering = ['id']

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    macroregion = models.ForeignKey(MacroRegion)

    class Meta:
        verbose_name_plural = "Регион"
        ordering = ['-id']

    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Страна"
        ordering = ['id']

    def __str__(self):
        return self.name


