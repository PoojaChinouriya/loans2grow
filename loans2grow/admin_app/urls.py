from django.urls import path
from .views import UserDetail, FamilyDetail, BankDetail

urlpatterns = [
    path('user/', UserDetail.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('family/', FamilyDetail.as_view()),
    path('family/<int:pk>/', FamilyDetail.as_view()),
    path('bank/', BankDetail.as_view()),
    path('bank/<int:pk>/', BankDetail.as_view()),

]    