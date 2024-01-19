from rest_framework import generics, status
from rest_framework.views import APIView
from application_generation.models import Application, Document 
from .serializers import ApplicationSerializer, DocumentSerializer, LoanSerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Loan

# email without attachment
from django.core.mail import EmailMessage
from django.core.mail import send_mail

# pdf and send email applications 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO

# logging 
import logging
error_logger = logging.getLogger('error_logger')
success_logger = logging.getLogger('success_logger')

class ApprovedLoanApplicationsListView(generics.ListAPIView):
    queryset = Application.objects.filter(status="document_verified", remark__icontains="approved by OH")
    serializer_class = ApplicationSerializer 
    success_logger.info('Applications with status=document_verified and remark approved by OH ')
   


# class ApprovedLoanApplication(APIView):
#     def get(self, request):
#         data = Application.objects.filter(status='document_verified', remark_icontains='approved by OH')
#         serializer = ApplicationSerializer(data, many=True)
#         return Response(serializer.data)


@api_view(http_method_names=['GET'])
def documentstoLSO(request, pk):
    try:
        document = Document.objects.get(application__id=pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data, status=200)
    except Exception as e:
        print(e)
        return Response(data={'detail':"Error"}, status=400)

@api_view(http_method_names=['PATCH'])
def doc_verification_lso(request, pk):  
    application = get_object_or_404(Application, id=pk)
    obj = Document.objects.get(application__id=pk)
    serializer = DocumentSerializer(data=request.data, instance=obj, partial=True)
    if serializer.is_valid():
        if obj.status == 'done' and obj.remark=="approved by LSO":
            obj.application.status = "sanctioned"
            obj.application.remark = "approved by LSO"
            obj.application.save() 
            serializer.save()
        elif obj.status == 'rejected' and obj.remark=='rejected by LSO':
            obj.application.status = "sanctioned"
            obj.application.remark = "approved by LSO"
            obj.application.save()
            serializer.save()
            #email functionality after document verification (rejected)
            email = EmailMessage(
            subject="Loan Sanction",
            body="Sorry, your loan application is rejected",
            to=[application.user.email,]
                                )
            email.send()
            #pass
        print(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET'])
def verified_doc_by_lso(request):
    try:
        objects = Document.objects.get(status="done", remark__icontains="verified by LSO")
        serializer = DocumentSerializer(objects)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(data={'detail':'Error'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['GET'])
def app_doc(request, pk):
    try:
        obj = Application.objects.get(id=pk)
        serializer = ApplicationSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(data={'detail':'Error'}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(http_method_names=['GET'])
# def all_applications(request):
#     try:
#         applications = Application.objects.all()
#         serializer = ApplicationSerializer(applications, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Exception as e:
#         print(e)
#         return Response(data={'detail':'Error'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(http_method_names=['GET'])
def all_applications(request):
    try:
        applications = Application.objects.filter(remark__icontains='approved by OH', status='document_verified')
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(data={'detail':'Error'}, status=status.HTTP_400_BAD_REQUEST)
    


    

    
@api_view(http_method_names=['POST'])
def emi(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        # Calculate Emi and total Payment
        id = int(data.get("id"))
        application = get_object_or_404(Application, pk=id)
        p = float(data.get("loan_principle"))
        t = int(data.get("loan_tenure"))
        ir = float(data.get("interest_rate"))
        ir_month = ir/12/100
        emi = p*ir_month*(1+ir_month)**t / ((1 + ir_month )**t - 1)
        processing_fee = 500
        total_payment = emi * t + processing_fee
        print(total_payment)

        # User Info
        first_name = application.user.first_name
        last_name = application.user.last_name

        # Calculate maturity date
        current_date = datetime.now()
        maturity_date = current_date + timedelta(days= t* 30)  # assuming 30 days per month
        print(maturity_date)

        # reportlab 
        buffer = BytesIO()
        buffer.name = f"LoanSanctionletter_{id}.pdf"

        # Title and content for the PDF
        pdf_title = "Loan Sanction Letter "
        pdf_content = [

            f"Mr {first_name} {last_name} your loan is sanctioned ",
            f"Your loan application details is given below",

            f"Your Application id is - {id}",
            f"Your Principle amount is - {p}",
            f"Your Loan tenure is - {t} month",
            f"Your Interest Rate Per Annum is - {ir}",
            f"Your Loan Sanctioning date is - {current_date}",
            f"Your Loan Maturity date is - {maturity_date}",
            f"Your Loan Emi is - {emi}",
            f"Your total_payment should be - {total_payment}",
           
        ]

        # Create PDF
        pdf = canvas.Canvas(buffer,pagesize=letter)

        # Set font and size
        pdf.setFont("Helvetica", 12)

        # Add title to the PDF
        pdf.drawCentredString(300, 750, pdf_title)

        # Add content to the PDF
        y_position = 730  # Starting y-position for content
        for line in pdf_content:
            pdf.drawString(50, y_position, line)
            y_position -= 20  # Adjust y-position for the next line

        # Save the PDF
        pdf.save()

        # send email functionality
        buffer.seek(0)
        email = EmailMessage(
            subject="Loan Sanction",
            body="Congratulations your loan application is approved",
            to=[application.user.email,]
        )
        email.attach(buffer.name,buffer.read(), 'application/pdf')
        email.send()

        # save data in the model 
        my_instance = Loan( application=application, loan_principal_amount=p, loan_tenure=t, 
                           interest_rate=ir,
                           total_amount_and_processing_fees= total_payment,installment=emi, 
                           maturity_date=maturity_date,
                           response_timestamp=current_date, status='done',
                           remark='Sanctioned by LSO')
 
        my_instance.save()
        return Response(status=status.HTTP_100_CONTINUE)
