from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth import login,logout,authenticate
from .forms import DetailsForms
def homepage(request):
    # return HttpResponse("Hello World! I'm Home.")
    data = models.Student.objects.all()
    # singledata = models.Student.objects.get(id=id)
    return render(request, 'home.html',{"data":data})


def about(request):
    # return HttpResponse("My About page.")
    form = DetailsForms()
    # if request.user.is_authenticated:
    #     if request.method == 'POST':
    #         name = request.POST.get('fname')
    #         Age  = request.POST.get('number')
    #         email = request.POST.get('email')
    #         Phone = request.POST.get('phone')
    #         print(name,Age,email,Phone)

    #         user = models.Student(name=name,Age=Age,email=email,Phone=Phone)
        
    #         user.save()
    #         # user.save(commit=True)
    #         return redirect('index')
    # else:
    #     return redirect('index')
    
    return render(request, 'about.html',{"form":form})


def data(request,id):
    singledata = models.Student.objects.get(id=id)
    return render(request, 'singledata.html',{"sin":singledata})

def delete(request,id):
    if request.user.is_authenticated:
        singledata = models.Student.objects.get(id=id)
        singledata.delete()
        return redirect('index')
    else:
        return redirect('index')
    
def update(request,id):
    data = models.Student.objects.get(id=id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('fname')
            Age  = request.POST.get('number')
            email = request.POST.get('email')
            Phone = request.POST.get('phone')
            data.name = name
            data.Age = Age
            data.email = email
            data.Phone = Phone
            data.save()
            return redirect('index')
    else:
        return redirect('index')
    
    return render(request,"edit.html", {"data":data})