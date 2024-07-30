from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
 

class Book(models.Model):
    title = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    date = models.DateField()


    def __str__(self) -> str:
        return self.author
    

    

