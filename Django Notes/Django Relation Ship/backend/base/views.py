from django.shortcuts import render,redirect
from .models import Book,Books
from .forms import BookForm,BooksForm

# Create your views here.

def getbook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request ,'create.html',{'form':form})

def View(request):
    books = Book.objects.all()
    return render(request, 'View.html',{'books':books})
    

