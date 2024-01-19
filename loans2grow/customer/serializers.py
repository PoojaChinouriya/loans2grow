from rest_framework import serializers
from customer.models import Enquiry
from admin_app.models import User



class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        exclude = ('status', 'response_timestamp')


    def create(self, validated_data):
        validated_data.setdefault('status','pending')
        return super().create(validated_data)
    

class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password']
        extra_kwargs = {'password':{'write_only':True}}


    
class LoginSerializer(serializers.Serializer):  
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)