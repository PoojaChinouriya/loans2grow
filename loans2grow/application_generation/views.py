
from rest_framework import generics, viewsets, status
from .serializers import ApplicationSerializer,ReportApplicationSerializer
from .models import Application
from rest_framework.response import Response
import datetime
from openpyxl import Workbook
from rest_framework.views import APIView
from io import BytesIO
 
class ApplicationViewSet(viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            data = request.query_params
            if 'status' in data:
                application = Application.objects.filter(status=data.get('status'))
                serializer = ApplicationSerializer(application, many = True)
                return Response (data=serializer.data, status=200)
            application = Application.objects.all()
            serializer = ApplicationSerializer(application, many = True)
            return Response (data=serializer.data, status=200)
        except Exception as e:
            return Response(data=None, status=400)    




class ReportApplicationViewSet(viewsets.GenericViewSet):
    serializer_class = ReportApplicationSerializer
    queryset = Application.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            data = request.query_params
            end_date = data.get('end_date')
            start_date= data.get('start_date')
            if 'start_date' in data and 'end_date' in data:
                application = Application.objects.filter(application_timestamp__range=(start_date, end_date))
                #applicationE = Application.objects.filter(application_timestamp=)
                serializer = ReportApplicationSerializer(application,many = True)
                return Response (data=serializer.data, status=200)
            application = Application.objects.all()
            serializer = ReportApplicationSerializer(application, many = True)
            return Response (data=serializer.data, status=200)
        except Exception as e:
            return Response(data=None, status=400)    


# class ApplicationStatusListView(generics.ListAPIView):
#     queryset =Application.objects.all()
#     serializer_class = ApplicationSerializer
    

#     def get_queryset(self):
#         status = self.request.query_params.get('status', None)
#         if status:
#             return Application.objects.filter(status=status)
#         return Application.objects.all()

# class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset =Application.objects.all()
#     serializer_class =ApplicationSerializer
   

#     # queryset = Application.objects.all()
#     # serializer_class =ApplicationSerializer
#     # filter_backends = [filters.SearchFilter]
#     # char_filter_fields = ['status']

# Create your views here.

# class  GeneratedApplicationListView(generics.ListAPIView):
#     queryset = Application.objects.filter(status="generated")
#     serializer_class = ApplicationSerializer


# class  SanctionedApplicationListView(generics.ListAPIView):
#     queryset = Application.objects.filter(status="sanctioned")
#     serializer_class = ApplicationSerializer


# class  DisbursedApplicationListView(generics.ListAPIView):
#     queryset = Application.objects.filter(status="generated")
#     serializer_class = ApplicationSerializer

# class  RejectedApplicationListView(generics.ListAPIView):
#     queryset = Application.objects.filter(status="rejected")
#     serializer_class = ApplicationSerializer

# class  DocumentVerifiedApplicationListView(generics.ListAPIView):
#     queryset = Application.objects.filter(status="document_verified")
#     serializer_class = ApplicationSerializer

# class JanApplicationFilter(generics.ListAPIView):
#     queryset=Application.objects.all()  
#     serializer_class =JanApplicationSerializer    
#     def get(self, request, *args, **kwargs):
#         start_date = datetime.datetime(2023, 1, 1) 
#         end_date = datetime.datetime(2023, 3, 31)
#         applications = Application.objects.filter(timestamp__range=(start_date, end_date))
#         serializer = self.get_serializer(applications, many=True)
#         return Response(data=serializer.data)
         




class ReportApplicationExcelView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = request.query_params
            id = request.query_params.get('id')
            end_date = data.get('end_date')
            start_date = data.get('start_date')

            if 'start_date' in data and 'end_date' in data:
                applications = Application.objects.filter(application_timestamp__range=(start_date, end_date))
            else:
                applications = Application.objects.all()

            serializer = ReportApplicationSerializer(applications, many=True)
            
            # Create Excel file
            workbook = Workbook()
            worksheet = workbook.active

            # Add headers
            headers = ['id', 'aadhaar_no','pan_no','type_of_employment',
                       'business_title','business_type','business_address',
                       'gst_registration_no','business_license_no',
                       'expected_average_annual_turnover','years_in_current_business',
                       'colletral','status','application_timestamp',
                       'remark','credit_score']  # Replace with your actual field names
            worksheet.append(headers)
            # worksheet['A1'] = 'id'
            # worksheet['B1'] = 'aadhaar_no'
            # worksheet['C1'] = 'pan_no'
            # worksheet['D1'] = 'type_of_employment'
            # worksheet['E1'] = 'business_title'
            # worksheet['F1'] = 'business_type'
            # worksheet['G1'] = 'business_address'
            # worksheet['H1'] = 'gst_registration_no'
            # worksheet['I1'] = 'business_license_no'
            # worksheet['J1'] = 'expected_average_annual_turnover'
            # worksheet['K1'] = 'years_in_current_business'
            # worksheet['L1'] = 'colletral'
            # worksheet['M1'] = 'application_timestamp'
            # worksheet['N1'] = 'remark'
            # worksheet['O1'] = 'credit_score'
       


            # Add data
            for row in serializer.data:
                worksheet.append([row['id'], row['aadhaar_no'],row['pan_no'],
                                 row['type_of_employment'],row['business_title'],row['business_type'],
                                 row['business_address'], row['gst_registration_no'],row['business_license_no'],
                                 row['expected_average_annual_turnover'],row['years_in_current_business'],
                                 row['colletral'],row['status'], row['application_timestamp'],
                                 row['remark'],row['credit_score']])
                # row['field3']])  # Replace with your actual field names

            # Save Excel file to a response
            # response = Response(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            # response['Content-Disposition'] = 'attachment; filename=report.xlsx'
            buffer = BytesIO()
            buffer.name = f"file_{start_date}+{end_date}.xlsx"
            workbook.save(buffer.name)

            return Response(data={'detail': "ok"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data={'detail': "Error"}, status=status.HTTP_400_BAD_REQUEST)
        
