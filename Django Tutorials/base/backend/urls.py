from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name="index"),
    path('about/', views.about, name="hello"),
    path('contact/<id>', views.data, name="contact"),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>',views.update, name = 'edit')
]
