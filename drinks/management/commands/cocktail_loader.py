from django.core.management.base import BaseCommand
from django.db import IntegrityError
from drinks.models import Drink
from ingredients.models import Ingredient
from recipes.models import  Recipe

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

        savedRecipe = 0
        duplicateRecipe = 0


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
                    for i in range(1,16):
                        ingredientname = item[f'strIngredient{i}']

                        if ingredientname != None and ingredientname!= '':
                            ingredient = Ingredient(
                                name = ingredientname,
                            )
                            try:
                                #Save the drink instance if it doesn't exist in database
                                ingredient.save()
                            except IntegrityError:
                                #If the drink already exists then get that drink object to use when saving recipe
                                duplicateIngredient += 1
                                ingredient = Ingredient.objects.get(name=ingredientname)
                            else:
                                savedIngredient += 1
                            finally:
                                if item[f'strMeasure{i}'] != None:
                                    recipe = Recipe(
                                        drink = drink,
                                        ingredient = ingredient,
                                        amount = item[f'strMeasure{i}']
                                    )
                                else:
                                    recipe = Recipe(
                                        drink = drink,
                                        ingredient = ingredient,
                                    )
                                try:
                                #Save the drink instance if it doesn't exist in database
                                    recipe.save()
                                except IntegrityError:
                                #If the drink already exists then get that drink object to use when saving recipe
                                    duplicateRecipe += 1
                                    # print(f'Drink: {drink} Ingredient:{ingredient}')
                                else:
                                    savedRecipe += 1
                                    print(f'Drink: {drink} Recipe: {recipe}')

        print(f'Total Attempted Cocktails: {totalAttemptedItems}')
        print(f'Total Saved Drinks: {savedDrink}')
        print(f'Total Duplicate Drinks: {duplicateDrink}')
        print(f'Total Saved Ingredients: {savedIngredient}')
        print(f'Total Duplicate Ingredients: {duplicateIngredient}')
        print(f'Total Saved Recipes: {savedRecipe}')
        print(f'Total Duplicate Recipes: {duplicateRecipe}')