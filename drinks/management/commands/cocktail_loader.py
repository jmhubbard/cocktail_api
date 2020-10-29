from django.core.management.base import BaseCommand
from django.db import IntegrityError
from drinks.models import Drink

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


        for item in cocktailsdict:
            totalAttemptedItems += 1
            #Create an instance of Show using the provided show name
            drink = Drink(
                name = item["strDrink"],
                instructions = item["strInstructions"],
            )
            if options["save"]:
                try:
                    #Save the show instance if it doesn't exist in database
                    drink.save()
                except IntegrityError:
                    #If the show already exists then get that shows object to use when saving episodes
                    duplicateDrink += 1
                    drink = Drink.objects.get(name=item["strDrink"])
                else:
                    savedDrink += 1
                # finally:
                #     #Create an instance of Episode using the provided episode name, season and the previous show instance
                #     episode = Episode(
                #         name = item["episode"],
                #         season = item["season"],
                #         show = show
                #     )
        print(f'Total Attempted Cocktails: {totalAttemptedItems}')
        print(f'Total Saved Drinks: {savedDrink}')
        print(f'Total Duplicate Drinks: {duplicateDrink}')