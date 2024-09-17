from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
