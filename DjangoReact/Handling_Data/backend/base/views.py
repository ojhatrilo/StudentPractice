from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
from django.contrib import messages     

# Create your views here.
def hello(request):
    if request.method == "POST":
        form = DataForm(request.POST)        
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error submitting data.')
    else:
        form = DataForm()
    return render(request, 'base.html', {"form": form})

def home(request):
    return HttpResponse("Thank you for submitting the data")
