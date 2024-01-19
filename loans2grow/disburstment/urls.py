from django.urls import path
from .views import  *

urlpatterns=[
    path('installment/<int:pk>/',InstallmentAPI.as_view()),
    path('default/',DefaultInstallmentsAPIView.as_view()),
    # path('default-user/<int:pk>/', UserAPIView.as_view())
    # path('installment/<int:pk>/',InstallmentView)
]
