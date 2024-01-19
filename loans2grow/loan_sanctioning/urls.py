from django.urls import path
from .views import ApprovedLoanApplicationsListView, documentstoLSO, doc_verification_lso, app_doc, verified_doc_by_lso
from .views import all_applications, emi


urlpatterns=[
    path('verified-oh/', ApprovedLoanApplicationsListView.as_view()),
    path('documents-to-LSO/<int:pk>/', documentstoLSO, name='documents-to-LSO-url'),
    path('doc_verification_lso/<int:pk>/', doc_verification_lso, name='document-verification-lso'),
    path('app-doc/<int:pk>/', app_doc, name='app-doc-url'),
    path('verified-doc-by-lso/', verified_doc_by_lso, name='veridied-doc-lso-url'),
    path('all_applications/', all_applications),
    path('emi/', emi)
]
   