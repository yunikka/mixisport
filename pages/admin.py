from django.contrib import admin

from .models import Pages

class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified', 'weight')
    search_fields = ('title', 'content')
    list_filter = ('enable', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Pages, PagesAdmin)