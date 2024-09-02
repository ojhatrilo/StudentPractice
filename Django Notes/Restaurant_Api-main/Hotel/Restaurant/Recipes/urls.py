from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.food_recipe_list),
    path('recipes/create/', views.food_recipe_create),
    path('recipes/update/<int:pk>/', views.food_recipe_update),
]