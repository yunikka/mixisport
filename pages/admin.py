from django.contrib import admin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import Pages

class PagesAdmin(MCEFilebrowserAdmin):
    list_display = ('title', 'created', 'modified', 'weight')
    search_fields = ('title', 'content')
    list_filter = ('enable', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Pages, PagesAdmin)