from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Musician,Album


# Create your views here.
def hello(request):
    query = Musician.objects.all()
    context = {"querys":query}    
    return render(request, 'index.html',context)

def hi(request):
    query = Album.objects.all()
    return render(request, 'famous.html',{"data":query})

