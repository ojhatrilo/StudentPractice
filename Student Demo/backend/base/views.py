from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Musician,Album
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def hello(request):
    query = Musician.objects.all()
    context = {"querys":query}    
    return render(request, 'index.html',context)

def hi(request):
    # query = Album.objects.get(id = id)
    if request.user.is_authenticated:
        if request.method =="POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            instrument = request.POST.get('instrument')

            value = Musician(first_name = fname,last_name = lname,instrument = instrument)
            value.save()
            return redirect('home')
    return render(request, 'famous.html')

def viewdata(request,id):
    query = Musician.objects.get(id = id)
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        instrument = request.POST.get('instrument')
        query.first_name = fname
        query.last_name = lname
        query.instrument = instrument
        query.save()        # value.save()
        return redirect("home")

    return render(request,'data.html',{"data":query})

def showdata(request,id):
    query = Musician.objects.get(id = id)
    return render(request,'showdata.html',{"data":query})


def delete(request,id):
    data = Musician.objects.get(id = id)
    data.delete()
    return redirect('home')

    
