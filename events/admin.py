from django.contrib import admin, messages

from .models import Fighters, EventPair, Events, Statistics, Battles, GalleryExtendedFighters

from photologue.admin import GalleryAdmin as GalleryAdminDefault
from photologue.models import Gallery


class FightersInline(admin.StackedInline):
    model = Statistics
    extra = 0
    fieldsets = [
        ('Побед/Поражений', {'fields': (('type','victory','defeat'),)}),
    ]

class FightersPairInline(admin.StackedInline):
    model = Battles
    extra = 0

class GalleryExtendedFightersInline(admin.StackedInline):
    model = GalleryExtendedFighters
    can_delete = False
    extra = 0

class FightersAdmin(admin.ModelAdmin):
    inlines = [FightersInline,FightersPairInline,GalleryExtendedFightersInline,]
    list_display = ('fullname', 'country', 'birthdate', 'height', 'weight', 'record')
    search_fields = ('fullname', 'country__name', 'height', 'weight', 'record', 'biography')
    list_filter = ('country',)
    prepopulated_fields = {'slug': ('fullname',)}

admin.site.register(Fighters, FightersAdmin)

def event_to_archive(modeladmin, request, queryset):
    for item in queryset:
        item.archive = True
        item.save()

    messages.add_message(request, messages.INFO, 'Событие(я) отправлено(ы) в архив')

event_to_archive.short_description = 'В архив'


class EventsInline(admin.StackedInline):
    model = EventPair
    extra = 0
    fieldsets = [
        ('Бойцы', {'fields': (('fighters_1','fighters_2',),('defeat_1','defeat_2',),('betting_odds_1','betting_odds_2',),('vote_1','vote_2',)),}),
        ('Способ победы/поражения', {'fields': (('result_type','result_round','result_time',),),}),
        ('Статистика', {'fields': (('punches_head_1','punches_head_2',),('punches_body_1','punches_body_2',),('kicks_head_1','kicks_head_2',),('kicks_body_1','kicks_body_2',),('throws_1','throws_2',),'content_stats','enable_stats'), 'classes': ['collapse',]}),
        ('Дополнительные настройки', {'fields': ('in_mainpage','weight',),}),
    ]

class EventsAdmin(admin.ModelAdmin):
    inlines = [EventsInline]
    list_display = ('name', 'location', 'archive',)
    search_fields = ('name', 'location', 'archive',)
    list_filter = ('location', 'start_time', 'archive',)
    prepopulated_fields = {'slug': ('name',)}
    actions = [event_to_archive,]

    
admin.site.register(Events, EventsAdmin)