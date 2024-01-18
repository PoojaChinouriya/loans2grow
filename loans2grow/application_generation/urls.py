from django.urls import path
from .views import ApplicationGenerationAPI, GuarantorGenerationAPI, DocumentGenerationAPI, FamilyGenerationAPI, BankGenerationAPI, UserGenerationAPI

urlpatterns = [
    path('application/', ApplicationGenerationAPI.as_view()),
    path('application/<int:pk>/', ApplicationGenerationAPI.as_view()),
    path('document/', DocumentGenerationAPI.as_view()),
    path('document/<int:pk>/', DocumentGenerationAPI.as_view()),
    path('guarantor/', GuarantorGenerationAPI.as_view()),
    path('guarantor/<int:pk>/', GuarantorGenerationAPI.as_view()),
    path('user/', UserGenerationAPI.as_view()),
    path('user/<int:pk>/', UserGenerationAPI.as_view()),
    path('family/', FamilyGenerationAPI.as_view()),
    path('family/<int:pk>/', FamilyGenerationAPI.as_view()),
    path('bank/', BankGenerationAPI.as_view()),
    path('bank/<int:pk>/', BankGenerationAPI.as_view()),

]
























# from django.urls import path
# from .views import ApplicationDetail, GuarantorDetail, DocumentDetail, ApplicationListView
# from .views import LoanRepApplicationDocumentView, LoanRepEnquiryListView


# urlpatterns = [
#     path('application/', ApplicationDetail.as_view()),
#     path('application/<int:pk>/', ApplicationDetail.as_view()),
#     path('guarantor/', GuarantorDetail.as_view()),
#     path('guarantor/<int:pk>/', GuarantorDetail.as_view()),
#     path('document/', DocumentDetail.as_view()),
#     path('document/<int:pk>/', DocumentDetail.as_view()),
#     path('applications/', ApplicationListView.as_view()),
#     path('api/loan-rep/applications/<int:application_id>/documents/', LoanRepApplicationDocumentView.as_view()),
#     path('api/loan-rep/enquiries/', LoanRepEnquiryListView.as_view()),
#     path('api/loan-rep/enquiries/<int:enquiry_id>/', LoanRepEnquiryListView.as_view()),  
# ]