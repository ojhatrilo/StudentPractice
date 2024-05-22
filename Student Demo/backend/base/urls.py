from django.urls import path
from . import views

urlpatterns =[
    path("", views.hello, name ='home'),
    path("name/<id>", views.hi, name="intro")
]