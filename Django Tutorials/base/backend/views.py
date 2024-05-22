from django.shortcuts import render
from django.http import HttpResponse
from . import models

def homepage(request):
    # return HttpResponse("Hello World! I'm Home.")
    data = models.Student.objects.all()

    return render(request, 'home.html',{"data":data})


def about(request):
    # return HttpResponse("My About page.")
    return render(request, 'about.html')


def data(request,id):
    singledata = models.Student.objects.get(id=id)
    return render(request, 'singledata.html',{"sin":singledata})