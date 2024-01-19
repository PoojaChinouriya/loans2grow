from django.contrib.auth.models import User
from rest_framework import serializers
from .models import FeedBack, Queries, FAQ
from django.core import validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['first_name', 'last_name', 'email', 'ratings', 'feedback_text']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model =  FAQ
        fields = '__all__'
   
def validate_answer_filled(value):
    if not value:
        raise serializers.ValidationError("Answer field must be filled when marking query as answered.")   

class QueriesSerializer(serializers.ModelSerializer):
       
     class Meta:
        model =  Queries
        fields = ['id', 'email', 'first_name', 'last_name', 'query','question_date']


class QueriesUpdateSerializer(serializers.ModelSerializer):
       
     class Meta:
        model =  Queries
        fields = "__all__"


        




   