from django.contrib import admin

from .models import Category, News, NewsGalleryExtended

from photologue.models import Gallery

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

admin.site.register(Category, CategoryAdmin)

class GalleryInline(admin.StackedInline):
    model = NewsGalleryExtended
    extra = 0

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created', 'modified')
    search_fields = ('title', 'content_preview', 'content_main')
    list_filter = ('status', 'owner', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}
    exclude = ('image',)
    inlines = [GalleryInline, ]
    

admin.site.register(News, NewsAdmin)
