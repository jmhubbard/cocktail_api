from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):

    list_display = ('drink', 'ingredient', 'amount',)
    list_filter = ('drink', 'ingredient', 'amount',)

admin.site.register(Recipe, RecipeAdmin)
