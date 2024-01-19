from rest_framework import serializers
from .models import Application, Document, Guarantor
from admin_app.serializers import UserSerializer

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class GuarantorSerializer(serializers.ModelSerializer):
     class Meta:
        model = Guarantor
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    documents= DocumentSerializer(read_only=True)
    guarantors = GuarantorSerializer(read_only=True, many=True)
    class Meta:
        model = Application
        fields = '__all__'
    
