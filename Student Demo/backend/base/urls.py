from django.urls import path
from . import views

urlpatterns =[
    path("", views.hello, name ='home'),
    path("name/", views.hi, name="intro")
]