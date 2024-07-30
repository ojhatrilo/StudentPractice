from django.forms import ModelForm
from .models import Book,Books

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'