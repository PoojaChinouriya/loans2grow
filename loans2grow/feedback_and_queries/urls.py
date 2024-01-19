from django.urls import path
from .views import FeedbackView, FAQView, QueriesView, QueryFetchView, QueriesDetailsAPI


urlpatterns = [
    path('feed/',FeedbackView.as_view(), name='feedback_view_url'),
    path('faq/',FAQView.as_view(), name='faq_view'),
    path('faq_delete/<int:pk>/',FAQView.as_view(), name='faq_view'),
    path('queries/',QueriesView.as_view(), name='queries_view_url'),
    path('query/',QueryFetchView.as_view(), name='queries_view_url'),
    path('query/<int:pk>/',QueriesDetailsAPI.as_view(), name='query-details'),
   
]