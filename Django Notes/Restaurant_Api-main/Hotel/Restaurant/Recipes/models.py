
from django.db import models

class FoodRecipe(models.Model):
    VEG = 'VEG'
    NON_VEG = 'NON-VEG'
    CATEGORY_CHOICES = [
        (VEG, 'Vegetarian'),
        (NON_VEG, 'Non-Vegetarian'),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name