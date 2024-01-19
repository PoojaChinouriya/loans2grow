from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, BankSerializer,Bank



class UserListCreateView(generics.ListCreateAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = User.objects.all()
        serializer_class = UserSerializer

class UserUpdateDeleteRetrivView(generics.RetrieveUpdateDestroyAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = User.objects.all()
        serializer_class = UserSerializer

class BankListCreateView(generics.ListCreateAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = Bank.objects.all()
        serializer_class = BankSerializer
