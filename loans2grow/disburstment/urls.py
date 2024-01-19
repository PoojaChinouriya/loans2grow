from django.urls import path
from .views import ApplicationDetailsView, DisbursementView, DisbursementDetailView, send_mail

urlpatterns = [
    path('aproval/', ApplicationDetailsView.as_view()),
    path('disb/', DisbursementDetailView.as_view()),
    path('disb/', DisbursementDetailView.as_view()),
    path('disb/<int:pk>/', DisbursementDetailView.as_view()),
    path('dis/<int:loan_id>/', DisbursementView.as_view()),
    path('send-mail/<int:pk>/', send_mail)
    
]