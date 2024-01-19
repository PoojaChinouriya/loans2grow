from rest_framework import viewsets, status
from rest_framework.response import Response #G
from .models import Document, Application
from .serializers import UploadSerializer, ApplicationSerializer
from rest_framework.views import APIView

from rest_framework.decorators import api_view

@api_view(http_method_names=['GET']) #G
def application(request):
    try:
        app = Application.objects.all()
        serializer = ApplicationSerializer(app, many=True)
        return Response(serializer.data , status=200)
    except Exception as e:
        print(e)
        return Response(data={'detail': 'Error'}, status=400)
        
        
class DocUploadAPIView(APIView):
    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


   

