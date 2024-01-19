from django.urls import path
from .views import application
from .views import DocUploadAPIView

urlpatterns = [
    path('app/', application),
    path('doc-upload/', DocUploadAPIView.as_view(), name='doc-upload-url'),

]