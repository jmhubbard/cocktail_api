from rest_framework import serializers
from .models import Drink
from recipes.serializers import RecipeSerializer

class DrinkSerializer(serializers.ModelSerializer):
    ingredients = RecipeSerializer(source='recipe_set', many=True)
    class Meta:
        model = Drink
        fields = ('name','instructions','ingredients')