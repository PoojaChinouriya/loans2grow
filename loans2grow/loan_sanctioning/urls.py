from django.urls import path
from .views import LoanView, VendorView

urlpatterns = [
    path('loan/<int:pk>/', LoanView.as_view(), name='loan-detail'),
    path('loan/', LoanView.as_view(), name='loan-list'),
    path('vendor/<int:pk>/', VendorView.as_view(), name='vendor-detail'),
    path('vendor/', VendorView.as_view(), name='vendor-list'),
]