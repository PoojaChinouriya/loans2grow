from django.shortcuts import render
from rest_framework import generics
from .models import Application, Guarantor, Document
from .models import Document
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ApplicationSerializer, GuarantorSerializer, DocumentSerializer


class ApplicationListCreateView(generics.ListCreateAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = Application.objects.all()
        serializer_class = ApplicationSerializer

class ApplicationRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = Application.objects.all()
        serializer_class = ApplicationSerializer

class GuarantorListCreateView(generics.ListCreateAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = Guarantor.objects.all()
        serializer_class = GuarantorSerializer


class document_verification(generics.ListCreateAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = Document.objects.all()
        serializer_class = DocumentSerializer

class document_modify(generics.RetrieveUpdateDestroyAPIView):
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        queryset = Document.objects.all()
        serializer_class = DocumentSerializer

        
