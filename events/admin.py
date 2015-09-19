from django.contrib import admin

from .models import Fighters, EventPair, Events

class FightersAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'country', 'birthdate', 'height', 'weight', 'record')
    search_fields = ('fullname', 'country', 'birthdate', 'height', 'weight', 'record', 'add_info')
    list_filter = ('country',)
    prepopulated_fields = {'slug': ('fullname',)}

admin.site.register(Fighters, FightersAdmin)

#class EventPairAdmin(admin.ModelAdmin):
#    list_display = ('name', 'fighters_1', 'fighters_2', 'in_mainpage')
#    search_fields = ('name', 'fighters_1', 'fighters_2')
#    list_filter = ('in_mainpage',)
#
#admin.site.register(EventPair, EventPairAdmin)

class EventsInline(admin.StackedInline):
    model = EventPair  
    extra = 0
    fieldsets = [
        ('Бойцы', {'fields': (('fighters_1','fighters_2',),('betting_odds_1','betting_odds_2',),)}),
        ('Харакетристики', {'fields': (('country_1','country_2',),('age_1','age_2',),('height_1','height_2',),('weight_1','weight_2',),('record_1','record_2',),)}),
        ('Дополнительные настройки', {'fields': ('in_mainpage',),}),
    ]
    
class EventsAdmin(admin.ModelAdmin):
    inlines = [EventsInline]
    list_display = ('name', 'location',)
    search_fields = ('name', 'location',)
    list_filter = ('location', 'start_time',) 
    prepopulated_fields = {'slug': ('name',)}

    
admin.site.register(Events, EventsAdmin)