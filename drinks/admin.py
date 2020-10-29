from django.contrib import admin

from .models import Drink


class DrinkAdmin(admin.ModelAdmin):

    list_display = ('name', 'instructions',)
    list_filter = ('name', 'instructions',)

admin.site.register(Drink, DrinkAdmin)
