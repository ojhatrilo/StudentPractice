from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models

def homepage(request):
    # return HttpResponse("Hello World! I'm Home.")
    # data = models.Student.objects.all()
    # singledata = models.Student.objects.get(id=id)

    return render(request, 'home.html',{"data":data})


def about(request):
    # return HttpResponse("My About page.")
    if request.method == 'Post':
        name = request.POST.get('fname')
        Age  = request.POST.get('number')
        email = request.POST.get('email')
        Phone = request.POST.get('phone')

        user = models.Student.objects.create(name=name,Age=Age,email=email,Phone=Phone)

        # user.save(commit=True)
        return redirect('index')
    return render(request, 'about.html')


def data(request,id):
    singledata = models.Student.objects.get(id=id)
    return render(request, 'singledata.html',{"sin":singledata})