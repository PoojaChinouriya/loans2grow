
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('loan_sanctioning.urls')),
    path('v1/', include('application_generation.urls')),
    path('v1/', include('admin_app.urls')),
    path('v1/', include('disburstment.urls')),
   
]
