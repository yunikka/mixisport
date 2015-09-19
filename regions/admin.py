from django.contrib import admin
from .models import MacroRegion, Region, Country

class RegionAdmin(admin.ModelAdmin):
    search_fields = ('name', 'macroregion')
    list_display = ('name', 'macroregion')

admin.site.register(Region, RegionAdmin)
admin.site.register(MacroRegion)
admin.site.register(Country)
