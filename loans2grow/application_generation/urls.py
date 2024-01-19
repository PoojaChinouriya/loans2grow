from . import views
from django.urls import path

urlpatterns=[
    path('applications/',views.ApplicationListCreateView.as_view()),
    path('document/',views.document_verification.as_view()),
    path('document/<int:pk>/',views.document_modify.as_view()),
    path('guranter',views.GuarantorListCreateView.as_view()),
    path('applications/<int:pk>/', views.ApplicationRetriveUpdateDestroyView.as_view())
]
