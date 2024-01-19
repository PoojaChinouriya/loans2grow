from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FeedBack, FAQ, Queries
from .serializers import FeedbackSerializer, FAQSerializer, QueriesSerializer, QueriesUpdateSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import generics



class FeedbackView(APIView):
    def get(self, request):
        feedbacks = FeedBack.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class FAQView(APIView):
   

    def get(self, request):
        queries = FAQ.objects.all()
        serializer = FAQSerializer(queries, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        try:
            serializer = FAQSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()                                  
            return Response(data=serializer.data, status=201)
        except Exception as e :
            print(e)
            return Response(serializer.errors, status=400)
        
    def delete(self, request, pk=None):
        try:
            faq = get_object_or_404(FAQ,pk=pk)
            faq.delete()
            return Response(status=204)
        except Exception as e:
            print(e)  
            return Response(status=400)

   
class QueriesView(APIView):


    def get(self, request):
        answers = Queries.objects.all()
        serializer = QueriesSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = QueriesSerializer(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
       
    
class QueryFetchView(APIView):
    def get(self, request):
        try:
            answers = Queries.objects.all()
            serializer = QueriesSerializer(answers, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str('answer_field')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = QueriesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str('answer_error')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class QueriesDetailsAPI(generics.RetrieveUpdateAPIView):
    serializer_class = QueriesUpdateSerializer
    queryset = Queries.objects.all()
    



