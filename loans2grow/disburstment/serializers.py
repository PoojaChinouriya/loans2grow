from rest_framework import serializers
from .models import *
from admin_app.models import User
from loan_sanctioning.models import  Loan
from application_generation.models import Application

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Application
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)
    class Meta:
        model = Loan
        fields = "__all__"


class InstallmentSerializers(serializers.ModelSerializer):
    loan = LoanSerializer(read_only=True)
    class Meta:
        model = Installment
        fields ="__all__"
     

class DefaulterSerializer(serializers.ModelSerializer):
    # defaulter = serializers.PrimaryKeyRelatedField(many=True, queryset=Defaulter.objects.all())
    class Meta:
        model =Defaulter
        # fields ='__all__'
        fields = ['id', 'user', 'default_amount', 'pending_since_date']

