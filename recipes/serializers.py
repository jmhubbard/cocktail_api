from rest_framework import serializers
from .models import Recipe
from ingredients.models import Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='ingredient.name')
    class Meta:
        model = Recipe
        fields = ['name','amount']