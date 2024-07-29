from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from random import randint

# def rand(self):
#     id =  randint(100000,999999)
#     self.id = id
    
# Create your models here.
class Student(models.Model):
    name =  models.CharField(max_length=100)
    Age =   models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    Phone = PhoneNumberField(null=False, blank=False, unique=True)
    id = models.BigAutoField(primary_key=True)


    def rand(self):
       id =  randint(100000,999999)
       self.id = id
    
       
    

    # def save(self):
    #     if not self.id:
    #         is_unique = False
    #         while not is_unique:
    #             id = randint(1000000, 9999999)  # 7-digit ID
    #             is_unique = not Student.objects.filter(id=id).exists()
    #         self.id = id
    #     super(Student, self).save()




    def __str__(self) -> str:
        return (f"{self.name,self.id}") 
