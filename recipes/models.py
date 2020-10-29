from django.db import models


class Recipe(models.Model):
    drink = models.ForeignKey(
        'drinks.Drink',
        on_delete=models.CASCADE,
    )
    ingredient = models.ForeignKey(
        'ingredients.Ingredient',
        on_delete=models.CASCADE,
    )
    amount = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.amount} {self.ingredient}'
