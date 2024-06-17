from django.urls import path
from . import views
urlpatterns = [
    # path('',views.getProducts, name = 'products'),
    # path('product/<int:id>',views.getproduct, name = 'product')
      path('api/items/', views.item_list, name='item-list'),
    path('api/items/<int:pk>/', views.item_detail, name='item-detail'),
    
]   


# myproject/urls.py

