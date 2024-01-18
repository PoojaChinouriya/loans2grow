from django.urls import path
from .views import EnquiryGenerationAPI

urlpatterns = [
    path('enquiries/', EnquiryGenerationAPI.as_view()),
    path('enquiries/<int:pk>/', EnquiryGenerationAPI.as_view()),
]