from django.contrib import admin

from .models import Category, News, GalleryExtended

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

admin.site.register(Category, CategoryAdmin)

class GalleryExtendedInline(admin.StackedInline):
    model = GalleryExtended
    extra = 0

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created', 'modified')
    search_fields = ('title', 'content_preview', 'content_main')
    list_filter = ('status', 'owner', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}
    exclude = ('image',)
    inlines = [GalleryExtendedInline, ]

admin.site.register(News, NewsAdmin)
