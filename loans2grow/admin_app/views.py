# from rest_framework.views import APIView, status
# from rest_framework.response import Response
# # from .serializers import UserSerializer, FamilySerializer, BankSerializer
# # , BankSerializer, FamilySerializer
# from .models import User, Family, Bank
# from django.shortcuts import get_object_or_404
# import logging
# from rest_framework.authtoken.models import Token
# # from django.contrib.auth import authenticate, login, logout
# # from .serializers import LoginSerializer
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated


# success_logger = logging.getLogger('success_logger')
# error_logger = logging.getLogger('error_logger')

    

# # class LoanRepresentativeLogin(APIView):
# #     def post(self, request, *args, **kwargs):
# #         serializer = LoginSerializer(data=request.data)
# #         if serializer.is_valid():
# #             email = serializer.validated_data['email']
# #             password = serializer.validated_data['password']

# #             user = authenticate(request, username=email, password=password)
# #             if user:
# #                 login(request, user)
# #                 token, created = Token.objects.get_or_create(user=user)
# #                 return Response({'token': token.key}, status=status.HTTP_200_OK)
# #             else:
# #                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# # class LoanRepresentativeLogout(APIView):
# #     authentication_classes = [TokenAuthentication]
# #     permission_classes = [IsAuthenticated]

# #     def post(self, request, *args, **kwargs):
# #         request.auth.delete()
# #         logout(request)
# #         return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)

        

