from django.core.management.base import BaseCommand
from django.db import IntegrityError
from drinks.models import Drink
from ingredients.models import Ingredient

from drinks.cocktailsdict import cocktailsdict

class Command(BaseCommand):
    help = 'Creates Drink from drinks.cocktailsdict'

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true', help='Save drinks to the database')

    def handle(self, *args, **options):
        totalAttemptedItems = 0
        #Show Counts
        savedDrink = 0
        duplicateDrink = 0
        #Character Counts
        savedIngredient = 0
        duplicateIngredient = 0


        for item in cocktailsdict:
            totalAttemptedItems += 1
            #Create an instance of Drink using the provided drink name and instructions
            drink = Drink(
                name = item["strDrink"],
                instructions = item["strInstructions"],
            )
            if options["save"]:
                try:
                    #Save the drink instance if it doesn't exist in database
                    drink.save()
                except IntegrityError:
                    #If the drink already exists then get that drink object to use when saving recipe
                    duplicateDrink += 1
                    drink = Drink.objects.get(name=item["strDrink"])
                else:
                    savedDrink += 1
                finally:
                    ingredientList = []
                    for i in range(1,16):
                        ingredientkey = f'strIngredient{i}'
                        ingredientList.append(item[ingredientkey])

                    for ingredient in ingredientList:
                        if ingredient != None:
                            newingredient = Ingredient(
                                name = ingredient
                            )
                            try:
                                #Save the drink instance if it doesn't exist in database
                                newingredient.save()
                            except IntegrityError:
                                #If the drink already exists then get that drink object to use when saving recipe
                                duplicateIngredient += 1
                                newingredient = Ingredient.objects.get(name=ingredient)
                            else:
                                savedIngredient += 1

        print(f'Total Attempted Cocktails: {totalAttemptedItems}')
        print(f'Total Saved Drinks: {savedDrink}')
        print(f'Total Duplicate Drinks: {duplicateDrink}')
        print(f'Total Saved Ingredients: {savedIngredient}')
        print(f'Total Duplicate Ingredients: {duplicateIngredient}')