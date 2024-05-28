from django.urls import path
from .views import create_item, item_list, item_detail, update_item, delete_item

urlpatterns = [
    path('', item_list, name='item_list'),
    path('item/<int:pk>/', item_detail, name='item_detail'),
    path('item/new/', create_item, name='create_item'),
    path('item/<int:pk>/edit/', update_item, name='update_item'),
    path('item/<int:pk>/delete/', delete_item, name='delete_item'),
]