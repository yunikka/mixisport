from django.contrib import admin

from .models import Fighters, EventPair, Events, Statistics, Battles

class FightersInline(admin.StackedInline):
    model = Statistics
    extra = 0
    fieldsets = [
        ('Побед/Поражений', {'fields': (('type','victory','defeat'),)}),
    ]

class FightersPairInline(admin.StackedInline):
    model = Battles
    extra = 0

class FightersAdmin(admin.ModelAdmin):
    inlines = [FightersInline,FightersPairInline]
    list_display = ('fullname', 'country', 'birthdate', 'height', 'weight', 'record')
    search_fields = ('fullname', 'country', 'birthdate', 'height', 'weight', 'record', 'biography')
    list_filter = ('country',)
    prepopulated_fields = {'slug': ('fullname',)}

admin.site.register(Fighters, FightersAdmin)

class EventsInline(admin.StackedInline):
    model = EventPair
    extra = 0
    fieldsets = [
        ('Бойцы', {'fields': (('fighters_1','fighters_2',),('defeat_1','defeat_2',),('betting_odds_1','betting_odds_2',),('vote_1','vote_2',)),}),
        ('Харакетристики', {'fields': (('country_1','country_2',),('age_1','age_2',),('height_1','height_2',),('weight_1','weight_2',),('record_1','record_2',), )}),
        ('Статистика', {'fields': (('punches_head_1','punches_head_2',),('punches_body_1','punches_body_2',),('kicks_head_1','kicks_head_2',),('kicks_body_1','kicks_body_2',),('throws_1','throws_2',),'content_stats','enable_stats'), 'classes': ['collapse',]}),
        ('Дополнительные настройки', {'fields': ('in_mainpage','weight',),}),
    ]
    
class EventsAdmin(admin.ModelAdmin):
    inlines = [EventsInline]
    list_display = ('name', 'location', 'archive',)
    search_fields = ('name', 'location', 'archive',)
    list_filter = ('location', 'start_time', 'archive',)
    prepopulated_fields = {'slug': ('name',)}

    
admin.site.register(Events, EventsAdmin)