from rest_framework import serializers
from .models import Drink
from recipes.serializers import RecipeSerializer
from django.urls import reverse, reverse_lazy
from django.http import request

class DrinkSerializer(serializers.ModelSerializer):
    ingredients = RecipeSerializer(source='recipe_set', many=True)
    drinktest = serializers.SerializerMethodField('add_text_to_drink')
    class Meta:
        model = Drink
        fields = ('id','name','ingredients','instructions', 'image', 'drinktest')

    def add_text_to_drink(self, drink):
        
        drinkname = f'http://sdlsjfsdlf/{drink.image}'
        return drinkname

