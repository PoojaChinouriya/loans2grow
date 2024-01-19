from rest_framework.views import APIView, status
from rest_framework.response import Response
from .serializer import ApplicationSerializer, DocumentSerializer, GuarantorSerializer
from .models import Application, Document, Guarantor


class ApplicationDetail(APIView):
    def get(Self, request, pk):
        try:
            application = Application.objects.get(pk=pk)
            serializer = ApplicationSerializer(application)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = ApplicationSerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GuarantorDetail(APIView):
    def get(self, request, pk):
        try:
            guarantor = Guarantor.objects.get(pk=pk)
            serializer = GuarantorSerializer(guarantor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = GuarantorSerializer(data=request.data, context={'request':request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DocumentDetail(APIView):
    def get(self, request, pk):
        try:
            documents = Document.objects.get(pk=pk)
            serializer = DocumentSerializer(documents)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = DocumentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

