from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ApplicationSerializer, GuarantorSerializer, DocumentSerializer, FamilySerializer, BankSerializer, UserSerializer
from .models import Application, Guarantor, Document
from loans2grow.utils import encode_application_id, SendApplicationMail, decode_application_id
from django.contrib.sites.shortcuts import get_current_site
from admin_app.models import Family, Bank, User
from django.urls import reverse
import logging
from django.shortcuts import get_object_or_404


success_logger = logging.getLogger('success_logger')
error_logger = logging.getLogger('error_logger')


class ApplicationGenerationAPI(generics.GenericAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            success_logger.info('Application data Fetched Successfully')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            error_logger.error(f'Error fetching Application data')
            return Response(data={'detail': 'Error Fetching Documents'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = serializer.data.get('user')
            print(user)
            application_id = serializer.data.get('id')
            b_app_id = encode_application_id(str(application_id))
            current_site =get_current_site(request=request).domain
            # relativeLink = reverse('document')
            # absurl ='http://'+current_site+relativeLink+"?app_id="+str(b_app_id)
            # # absurl = f'http://localhost:3000/document/{b_app_id}
            # email_body = 'Hello,'+user.get('first_name')+ 'use the link below to upload your documents\n'+absurl
            # data = {'email_body': email_body, 'subject':'Upload your Documents', 'to':user.get() }
            # SendApplicationMail.send_mail(data=data)
            success_logger.info(f'Application created with username {user.get("email")}')
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            error_logger.error(f"Error creating Application {serializer.errors}")
            return Response(data= serializer.errors, status=400)
        

    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            success_logger.info(f'Application updated with id ')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            error_logger.error(f"Error updating Application")
            return Response(data={'detail': 'Error updating Application'}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            success_logger.info(f'Application deleted with id')
            return Response(data={'detail': 'Application deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            error_logger.error(f"Error deleting Application ")
            return Response(data={'detail': 'Error deleting Application'}, status=status.HTTP_400_BAD_REQUEST)
        
class GuarantorGenerationAPI(generics.GenericAPIView):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer 

    
    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            success_logger.info(f'guarantor data Fetched Successfully')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f'Error fetching Guarantor data')
            return Response(data={'detail': 'Error Fetching Documents'}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            application = serializer.data.get('application')
            print(application)
            # guarantor_id =  serializer.data.get('id')
            # b_app_id = encode_application_id(str(guarantor_id))
            # current_site = get_current_site(request=request).domain
            success_logger.info(f"Guarantor created with application ")
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            error_logger.error(f"Error creating Guarantor {serializer.errors}")
            return Response(data= serializer.errors, status=400)
        

class DocumentGenerationAPI(generics.GenericAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer 

    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            success_logger.info(f'documents data Fetched Successfully')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f'Error fetching documents data')
            return Response(data={'detail': 'Error Fetching Documents'}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            success_logger.info(f"documents created with application ")
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_logger.error(f"Error creating documents {serializer.errors}")
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserGenerationAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'detail': 'Error Fetching user'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        
class FamilyGenerationAPI(generics.GenericAPIView):
    serializer_class = FamilySerializer
    queryset = Family.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            success_logger.info(f'Family data Fetched Successfully')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f'Error fetching Guarantor data')
            return Response(data={'detail': 'Error Fetching Family Data'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            success_logger.info(f"Family created with application ")
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_logger.error(f"Error creating family {serializer.errors}")
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BankGenerationAPI(generics.GenericAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            success_logger.info(f'bank data Fetched Successfully')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f'Error fetching bank data')
            return Response(data={'detail': 'Error Fetching Banks'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            success_logger.info(f"bank created with application ")
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_logger.error(f"Error creating bank {serializer.errors}")
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            




    



























# class LoanRepSendMailView(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, request, application_id, format=None):
#         try:
#             application = Application.objects.get(id=application_id)
#             application_id = ''
#             customer_email = ''
#             subject = 'Application Submission Confirmation'
#             message = f'Thank you for submitting your application! Your application ID is: {application_id}'
#             from_email = ''  
#             recipient_list = [customer_email]
#             send_mail(subject, message, from_email, recipient_list)
#             success_logger.info(f"Email sent by loan representative to {recipient_list} for loan application status update")
#             serializer = ApplicationSerializer(application)
#             return Response({'detail': 'Email sent successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

#         except Application.DoesNotExist:
#             error_logger.info(f"Application does not found")
#             return Response({'detail': 'Application not found'}, status=status.HTTP_404_NOT_FOUND)