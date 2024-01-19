from .views import *
# GeneratedApplicationListView,RejectedApplicationListView,DisbursedApplicationListView,DocumentVerifiedApplicationListView,SanctionedApplicationListView
from django.urls import path

urlpatterns=[
    path('applicationview/', ApplicationViewSet.as_view({'get': 'list'}) ),
    path('reports/', ReportApplicationViewSet.as_view({'get': 'list'}) ),
    path('reportxl/', ReportApplicationExcelView.as_view()),

    # path('application-status/', ApplicationStatusListView.as_view(),name='application-status-list' )
    # path('generated/', GeneratedApplicationListView.as_view()),
    # path('rejected/', RejectedApplicationListView.as_view()),
    # path('disbursed/', DisbursedApplicationListView.as_view()),
    # path('documentverified/', DocumentVerifiedApplicationListView.as_view()),
    # path('sanctioned/', SanctionedApplicationListView.as_view()),
    # path('users/', ApplicationStatusListView.as_view(), name='user-list'),
    # path('users/<int:pk>/', ApplicationDetailView.as_view(), name='user-detail'),
    
]