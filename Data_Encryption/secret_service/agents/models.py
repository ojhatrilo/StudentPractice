

# Create your models here.
from django.db import models

class Agent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    badge_no = models.CharField(max_length=10, unique=True)
    code_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    secret_mission = models.TextField()
    active = models.BooleanField()
    no_of_assignments = models.IntegerField()