from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serializers import UserSerializer, FamilySerializer, BankSerializer
from .models import User, Family, Bank

class UserDetail(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class FamilyDetail(APIView):
    def get(self, request, pk):
        try:
            family = Family.objects.get(pk=pk)
            serializer = FamilySerializer(family)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = FamilySerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BankDetail(APIView):
    def get(self, request, pk):
        try:
            bank = Bank.objects.get(pk=pk)
            serializer = BankSerializer(bank)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = BankSerializer(data=request.data)
            serializer.is_valid()
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                

