from django.urls import path
from . import views


urlpatterns = [
    path("",views.hello, name="data"),
    path("home/",views.home, name="home")
]