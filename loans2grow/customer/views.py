from rest_framework import viewsets, response, generics
from .serializers import EnquirySerializer, LoginSerializer, UserRegSerializer
from rest_framework.response import Response
from customer.models import Enquiry
from .utils import send_otp, check_otp
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class EnquiryViewSet(viewsets.GenericViewSet):
    serializer_class = EnquirySerializer
    queryset = Enquiry.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            otp = request.data.get("otp")
            mobile = request.data.get("mobile")
            mobile = "+"+mobile
            verification_check = check_otp(mobile=mobile, otp=otp)
            print(verification_check)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if verification_check == "approved":
                serializer.save()
                return response.Response(data=serializer.data, status=201)
            return response.Response(data={'details':'OTP is invalid'},status=400)
        except Exception as e:
            print(e)
            return response.Response(data=serializer.error, status=400)
        

    @action(methods=['get'], detail=False)
    def send_otp(self, request, *args, **kwargs):
        try:
            mobile = request.query_params.get('mobile')
            mobile="+"+mobile
            verification = send_otp(mobile=mobile)
            return response.Response(data={'verification_status':verification}, status=200)
        except Exception as e:
            print(e)
            return response.Response(data={'deatils':'Error'}, status=400)



# class UserAPI(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     @api_view(['POST'])
#     def register_user(request):
#         if request.method == 'POST':
#             serializer = LoginSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=201)
#             return Response(serializer.error, status=400)

# class RegisterView(generics.CreateAPIView):
#     queryset = Enquiry.objects.all()
#     serializer_class = UserRegSerializer
    


# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data['email']
#         password = serializer.validated_data['password']

#         user = authenticate(request, email=email, password=password)
#         if user:
#             login(request, user)
#             return Response({'message':'login successfully'}, status=200)
#         else:
#             return Response({'message':'Invalid credentials'},status=400)
        

# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({'message':'Logout successfully'})


    # @api_view(['POST'])
    # def user_logout(request):
    #     logout(request)
    #     return Response({'message':'Logout successfully'})



#     @api_view(['POST'])
#     def user_login(request):  
#         if request.method == 'POST':
#             # username = request.data.get('username')
#             # password = request.data.get('password')       
#             serializer = UserSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             user = serializer.validated_data['user']
#             login(request, user)
#             return Response({'message':'Loggin successfully'})



        