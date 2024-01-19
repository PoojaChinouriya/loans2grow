from .models import *
from .serializers import *
# from rest_framework import generics,viewsets
from rest_framework import status, viewsets,generics
from django .shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from datetime import date, timedelta
from application_generation.models import Application
from admin_app.models import User 

class InstallmentAPI(APIView):

    def get(self, request,pk):
        # posts = Installment.objects.all()#query set
        try:
            installment = Installment.objects.filter(loan__application__id=pk)
            serializer = InstallmentSerializers(installment, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK )
        except Exception as e:
            print(e)
            return Response(data={'detail':"Error"}, status=400)
        # serializer = InstallmentSerializers(posts, many=True)#it will serialize queryset
        # print(serializer.data)#json serialable data



class DefaultInstallmentsAPIView(generics.ListCreateAPIView):
    queryset = Installment.objects.filter(installment_expected_date__lt=date.today() - timedelta(days=90))
    serializer_class = InstallmentSerializers

    def create(self, request, *args, **kwargs):
        # Get the overdue installments
        try:
            overdue_installments = self.get_queryset()
        
        # Add users to the Defaulter list
            for installment in overdue_installments:
               user = installment.loan.application.user
               defaulter, created = Defaulter.objects.get_or_create(user=user)
            
            if created:
                defaulter.default_amount += installment.remaining_amount
                defaulter.pending_since_date = installment.installment_expected_date
                defaulter.save()

        # Return a response
                return Response(user,{'message': 'Defaulters added successfully'})
        except Exception as e:
            print(e)
            return Response(data={'detail':"Error"}, status=400)

    
    
    
    
    #def get(self, request,pk):
    
# class UserAPIView(APIView):
#     def get(self, request,pk):
#         # posts = Installment.objects.all()#query set
#         try:
#             # Installment = get_object_or_404(id=pk)
#             user = User.objects.filter(installment__loan__application__user__id=pk) # feching error
#             print('After user')
#             serializer = UserSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK )
#         except Exception as e:
#             print(e)
#             return Response(data={'detail':"Error"}, status=400)




# class DefaulterAPI(APIView):
#     # queryset = Defaulter.objects.all()
#     # serializer_class = DefaulterSerializer
#     def get(self, request,pk):
#         # posts = Installment.objects.all()#query set
#         try:
#             defaulter = Defaulter.objects.filter(id=pk)
#             serializer = DefaulterSerializer(defaulter, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK )
#         except Exception as e:
#             print(e)
#             return Response(data={'detail':"Error"}, status=400)
        
        
#     def get(self, request, pk):
#         try:
#             defaulter = get_object_or_404(Defaulter, id=pk)
#             serializer = DefaulterSerializer(defaulter)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return Response(data={'detail': "Error"}, status=status.HTTP_400_BAD_REQUEST)


# class DefaulterAPI(APIView):
#     def get(self, request, pk):
#         try:
#             # user = get_object_or_404(User, pk=id)
#             defaulter = Defaulter.objects.filter(user__id=pk)
#             serializer = DefaulterSerializer(defaulter)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return Response(data={'detail': "Error"}, status=status.HTTP_400_BAD_REQUEST)
# class DefaulterAPI(APIView):
#     queryset = Defaulter.objects.all()
#     serializer_class = DefaulterSerializer
# class  DefaulterAPI(generics.ListAPIView):
#     # defaulter = serializers.PrimaryKeyRelatedField(many=True)
#     queryset = Defaulter.objects.all()
    # serializer_class = DefaulterSerializer
       
    
# @api_view(http_method_names=['GET'])
# def InstallmentView(request, pk):
#     try:
#         installment = Installment.objects.get(Installment__id=pk)
#         serializer = InstallmentSerializers(installment)
#         return Response(serializer.data, status=200)
#     except Exception as e:
#         print(e)
#         return Response(data={'detail':"Error"}, status=400)


# class InstallmentViewset(viewsets.ListAPIView):
#     queryset = Installment.objects.all()
#     serializer_class= InstallmentSerializers
#     return Response(data = serializer.data, status=status.HTTP_200_OK )


#     queryset=Application.objects.all()  
#     serializer_class =JanApplicationSerializer    
#     def get(self, request, *args, **kwargs):
#         start_date = datetime.datetime(2023, 1, 1) 
#         end_date = datetime.datetime(2023, 3, 31)
#         applications = Application.objects.filter(timestamp__range=(start_date, end_date))
#         serializer = self.get_serializer(applications, many=True)
#         return Response(data=serializer.data)
         
