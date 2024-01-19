from rest_framework import serializers
from .models import Defaulter, Installment, Disbursement
from loan_sanctioning.models import Loan, Vendor
from admin_app.models import User, Family, Bank
from application_generation.models import Document, Guarantor, Application
from admin_app.serializers import FamilySerializer, BankSerializer, UserSerializer
from application_generation.serializer import ApplicationSerializer, DocumentSerializer, GuarantorSerializer
from loan_sanctioning.serializers import LoanSerializer, VendorSerializer
from phonenumber_field.modelfields import PhoneNumberField

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Bank
        fields = '__all__'

   
class DocumentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Document
        fields = '__all__'

class GuarantorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Guarantor
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__' 

class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Loan
        fields = '__all__' 

class UserSerializer(serializers.ModelSerializer):
    family = FamilySerializer(read_only=True)
    banks = BankSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = fields = ('id','first_name', 'last_name','email', 'gender', 'mobile', 'permanent_address', 'current_address','dob','role', 'family', 'banks')

class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    guarantor = GuarantorSerializer(read_only=True, many=True)
    documents = DocumentSerializer(read_only=True)
    Loans = LoanSerializer(read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'


class DefaulterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defaulter
        fields = '__all__'

class InstallmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Installment
        fields = '__all__'

class DisbursementSerializer(serializers.ModelSerializer):
    #loan = LoanSerializer(read_only = True) 
    
    
    class Meta:
        model = Disbursement
        fields = '__all__'

    
    

    