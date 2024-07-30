from django.urls import path
from . import views

urlpatterns = [
    path('',views.View, name ='view'),
    path('create/',views.getbook, name ='create'),

]
