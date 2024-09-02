from django.shortcuts import render,redirect
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.
@login_required
def home(request):
    data3 = models.student.objects.all().values()
    return render(request, 'index.html',{'data':data3})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
    return render (request,"Register.html")

@csrf_exempt
def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password' ]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def view_logout(request):
    logout(request)
    return redirect('login')