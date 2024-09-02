from django.urls import path
from . import views
urlpatterns = [
    path("home/",views.home, name="home"),
    path("",views.view_login, name="login"),
    path("register/",views.register, name="register"),
    path("logout/",views.view_logout, name="logout"),

]