from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created',)
    search_fields = ('title', 'category', 'created',)
    list_filter = ('category', 'created',)
#    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Video, VideoAdmin)