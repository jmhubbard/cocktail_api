from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Drink
from .serializers import DrinkSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/drink-list/',
        'Detail View': '/drink-detail/<str:pk>/',
        'Drinks By Letter': '/drink-by-letter/<str:pk>/',
        'Create': '/drink-create/',
        'Update': '/drink-update/<str:pk>/',
        'Delete': '/drink-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def drinkList(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def drinkDetail(request, pk):
    drink = Drink.objects.get(id=pk)
    serializer = DrinkSerializer(drink, many=False)

    return Response(serializer.data)

@api_view(['Get'])
def drinksByLetter(request, pk):
    drinks = Drink.objects.filter(name__startswith=pk)
    serializer = DrinkSerializer(drinks, many=True)

    return Response(serializer.data)
