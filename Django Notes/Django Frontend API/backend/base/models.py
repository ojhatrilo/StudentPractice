from django.db import models



class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()



class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


