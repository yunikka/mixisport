from .models import Seo

class SeoTags:

    @staticmethod
    def title():
        try:
            title = Seo.objects.get(tag=1)
        except:
            title = None
        return title

    @staticmethod
    def description():
        try:
            description = Seo.objects.get(tag=2)
        except:
            description = None
        return description

    @staticmethod
    def keywords():
        try:
            keywords = Seo.objects.get(tag=3)
        except:
            keywords = None
        return keywords
