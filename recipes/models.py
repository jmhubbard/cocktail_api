from django.db import models

from drinks.models import Drink
from ingredients.models import Ingredient

class Recipe(models.Model):
    drink = models.ForeignKey(
        Drink,
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
    )
    amount = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.amount} {self.ingredient}'
