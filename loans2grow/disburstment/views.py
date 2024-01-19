from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Defaulter, Installment, Disbursement
from .serializers import  DisbursementSerializer, ApplicationSerializer
from loan_sanctioning.models import Loan
from application_generation.models import Application, Document, Guarantor
from admin_app.models import User, Bank
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from rest_framework.decorators import api_view
import smtplib

class ApplicationDetailsView(APIView):
    def get(self, request):
        try:
            applications = Application.objects.filter(
                #status='done',
                remark__icontains='approved by LSO'   
            )
           
            serializer = ApplicationSerializer(applications, many=True)
            serializer_data = serializer.data

            return Response(serializer_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': f'Error: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        
class DisbursementView(APIView):    

    def get(self, request, loan_id):
        try:
            loan = Loan.objects.get(id=loan_id)
            
            gst_percentage= 18
            gst_amount = (gst_percentage/100)*(loan.loan_principal_amount)

            total_gross_price = loan.loan_principal_amount
            total_gst_amount = gst_amount

            disbursement_data = {
                'loan': loan.id,
                'net_disbursed_amount': loan.loan_principal_amount - gst_amount,
                'total_gross_price': total_gross_price,
                'total_gst_amount': total_gst_amount,
                'status': 'disbursed',
            }

            return Response(disbursement_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': f'Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            serializer = DisbursementSerializer(data=request.data,)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'detail': 'Disbursement saved successfully.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'detail': f'Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class DisbursementDetailView(APIView):
    def get(self, request):
        try:
            disbursement = Disbursement.objects.filter(status='disbursed')
            serializer = DisbursementSerializer(disbursement, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            serializer = DisbursementSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
                
            return Response({'detail': 'Disbursement saved successfully.'}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            print(e)
            return Response({'detail': f'Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        

@api_view(http_method_names=['GET'])
def send_mail(request, pk):
        disbursement = get_object_or_404(Disbursement, pk=pk)
        
        
        if disbursement.status == 'disbursed' :
            
            #serializer.save()
            print(1)

            email_subject = "Loan Disbursed"
            email_body = "Congratulations, your loan is disbursed."
            recipient_email = disbursement.loan.application.user.email

            email = EmailMessage(subject=email_subject, body=email_body, to=[recipient_email])
            email.send()
            print(2)
            return Response(status=status.HTTP_200_OK)
        return Response( status=status.HTTP_400_BAD_REQUEST)


