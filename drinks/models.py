from django.db import models
from ingredients.models import Ingredient
from recipes.models import Recipe

class Drink(models.Model):
    name = models.CharField(max_length=200, unique=True)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='recipes.Recipe')
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name
