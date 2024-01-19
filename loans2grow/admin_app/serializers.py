from rest_framework import serializers
from .models import Bank, Family
from django.contrib.auth import get_user_model
User = get_user_model()


class FamilySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Family
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bank
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    family=FamilySerializer(read_only=True)
    banks=BankSerializer(read_only=True, many=True)
    password2 = serializers.CharField(style={'input_type': 'password'}
                                      , write_only=True)
    id = serializers.IntegerField(read_only=True)
    date_joined=serializers.DateTimeField(read_only=True)
    is_superuser=serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        exclude = ['user_permissions', 'groups']
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('password & password 2 must be same')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
       