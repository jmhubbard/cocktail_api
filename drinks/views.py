from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Drink
from .serializers import DrinkSerializer

from django.views.generic.base import TemplateView

def getRandomDrink():
    import random
    drinks = Drink.objects.all()
    drinklist = []
    for item in drinks:
        drinklist.append(item.id)
    randomDrinkId = random.choice(drinklist)
    randDrink = Drink.objects.get(id = randomDrinkId)
    return randDrink


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/drink-list/',
        'Detail View': '/drink-detail/<str:pk>/',
        'Drinks By Letter': '/drink-by-letter/<str:firstChar>/',
        'Ingredients List': '/ingredient-list/',
        'Random Drink': '/random-drink/',
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
def drinksByLetter(request, firstChar):
    drinks = Drink.objects.filter(name__istartswith=firstChar)
    serializer = DrinkSerializer(drinks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def randomDrink(request):
    randDrink = getRandomDrink()
    serializer = DrinkSerializer(randDrink, many=False)

    return Response(serializer.data)