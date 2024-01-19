from rest_framework import serializers
from application_generation.models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"



class ReportApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields ="__all__"