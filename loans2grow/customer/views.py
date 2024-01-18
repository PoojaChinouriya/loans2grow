from rest_framework import generics, status
from .models import Enquiry
from .serializers import EnquirySerializer
import logging
from rest_framework.response import Response

success_logger = logging.getLogger('success_logger')
error_logger = logging.getLogger('error_logger')

class EnquiryGenerationAPI(generics.GenericAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

    def get(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            success_logger.info(f'Enquiry data Fetched Successfully')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_logger.error(f'Error fetchingenquiry data')
            return Response(data={'detail': 'Error Fetching Documents'}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            success_logger.info(f"Enquiry created with application ")
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_logger.error(f"Error creating Enquiry {serializer.errors}")
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)