from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.TextField()
    
    def __str__(self):
        return self.name
