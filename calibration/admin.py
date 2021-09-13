from django.contrib import admin
from .models import User, Coffee, Espresso, Filter


""" Admin customisation section """
admin.site.site_header = "Calibration Admin Page"

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ("name", "origin", "process")


admin.site.register(User)
admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Espresso)
admin.site.register(Filter)
