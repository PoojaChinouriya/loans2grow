from rest_framework import serializers
from .models import  Document, Application


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

        

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        


