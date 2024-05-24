from django.urls import path
from . import views

urlpatterns =[
    path("", views.hello, name ='home'),
    path("form/", views.hi, name="intro"),
    path("data/<id>",views.viewdata, name = "data")
]