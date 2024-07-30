from django.contrib import admin

# Register your models here.
from .models import Book,Books

admin.site.register(Books)
admin.site.register(Book)

