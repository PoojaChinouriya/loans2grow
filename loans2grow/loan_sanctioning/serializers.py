from rest_framework import serializers
from application_generation.models import Application, Document
from .models import Loan

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__' 

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

    def update(self, instance, validated_data):
        from datetime import datetime
        instance.status = validated_data.get('status')
        instance.remark = validated_data.get('remark', 'approved by LSO')
        instance.response_timestamp = datetime.today()
        return instance
    
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'