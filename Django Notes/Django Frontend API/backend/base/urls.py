# from django.urls import path
# from .views import ProfileList, ProfileDetail

# urlpatterns = [
#     path('profiles/', ProfileList.as_view(), name='profile-list'),
#     path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
# ]


from django.urls import path
from .views import ProfileDetail,ProfileList

urlpatterns = [
    path("profile/<int:pk>/",ProfileDetail.as_view(), name='profile-detail'),
    path("", ProfileList.as_view(), name='profile-list')
]