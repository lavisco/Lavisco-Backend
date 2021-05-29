from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserListSerializer
from .models import CustomUser
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserListSerializer
    queryset = CustomUser.objects.all()
