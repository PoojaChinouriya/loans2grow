from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customer.views import EnquiryViewSet
from application_generation.views import DocUploadAPIView
from django.conf import settings
from django.conf.urls.static import static   
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
# from application_generation.views import  ApplicationViewSet # dont delete


router = DefaultRouter()
router.register('enquiry', EnquiryViewSet, basename='enquiry')
#router.register('document', DocUploadAPIView, basename='document')
#router.register('application', ApplicationViewSet, basename='application')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)), 
    path('v1/', include('application_generation.urls')), # G
    path('v1/', include('customer.urls')), # G
    path('v1/access/', token_obtain_pair),
    path('v1/refresh/', token_refresh)
]

urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
