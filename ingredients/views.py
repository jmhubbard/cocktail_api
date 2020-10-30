from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ingredient
from .serializers import IngredientSerializer

@api_view(['GET'])
def ingredientList(request):
    ingredients = Ingredient.objects.all().order_by('name')
    serializer = IngredientSerializer(ingredients, many=True)

    return Response(serializer.data)
