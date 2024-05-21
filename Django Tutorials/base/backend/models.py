from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    name =  models.CharField(max_length=100)
    Age =   models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    Phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return (f"{self.name}") 
