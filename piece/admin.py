from django.contrib import admin

from .models import Slider, SliderItem, Ticker, Seo, SocialIcons, Commerce

class SliderInline(admin.TabularInline):
    model = SliderItem    
    
class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderInline]
    list_display = ('name', 'enable')
    search_fields = ('name',)
    list_filter = ('enable', 'name')    
    
admin.site.register(Slider, SliderAdmin)

class TickerAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'enable')
    search_fields = ('name', 'text',)
    list_filter = ('name', 'text', 'enable') 
    
admin.site.register(Ticker, TickerAdmin)

class SeoAdmin(admin.ModelAdmin):
    list_display = ('tag', 'code',)
    search_fields = ('tag', 'code',)
    list_filter = ('tag',)
    
admin.site.register(Seo, SeoAdmin)

class SocialIconsAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'url', 'icon_code',)
    search_fields = ('name', 'url', 'icon_code',)
    list_filter = ('name',)

admin.site.register(SocialIcons, SocialIconsAdmin)

class CommerceAdmin(admin.ModelAdmin):
    list_display = ('code_type','enable',)
    search_fields = ('code_type', 'codetext',)
    list_filter = ('enable',)

admin.site.register(Commerce, CommerceAdmin)