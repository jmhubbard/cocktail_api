from django.db import models
from ingredients.models import Ingredient
from recipes.models import Recipe

class Drink(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='recipes.Recipe')
    
    def __str__(self):
        return self.name
