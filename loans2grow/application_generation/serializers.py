from rest_framework import serializers
from admin_app.models import User, Family, Bank
from application_generation.models import Application, Document, Guarantor
from phonenumber_field.modelfields import PhoneNumberField


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class GuarantorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guarantor
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Document
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    family = FamilySerializer( read_only=True)
    banks = BankSerializer(many=True, read_only=True)
    
   

    # username = serializers.CharField()
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    # email = serializers.EmailField()
    # #is_active = serializers.BooleanField(default=False, write_only=True)
    # mobile = PhoneNumberField()
    # role = serializers.CharField(default="cs")
    # gender = serializers.ChoiceField(choices=User.GENDER_CHOICES)
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','email', 'gender', 'mobile', 'permanent_address', 'current_address','dob','role', 'family', 'banks')


class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    guarantors = GuarantorSerializer(read_only=True, many=True)
    documents = DocumentSerializer(read_only=True)

    class Meta:
        model = Application
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.pop('user')
        user = User.objects.create_user(**user)
        application = Application.objects.create(user=user, **validated_data)
        return application
    

    












    # def create(self, validated_data):
    #     user = validated_data.pop('user')
    #     user = User.objects.create_user(**user)
    #     guarantor = Guarantor.objects.create(user=user, **validated_data)
    #     return guarantor




#     def create(self, validated_data):
#         user = validated_data.pop('user')
#         user = User.objects.create_user(**user)
#         document = Document.objects.create(user=user, **validated_data)
#         return document






































# from rest_framework import serializers
# from .models import Application, Guarantor, Document
# from datetime import date
# from django.contrib.auth import get_user_model


# User = get_user_model()

# class GuarantorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Guarantor
#         fields = '__all__'

#     def validate_email(self, value):
#         if get_user_model().objects.filter(email=value).exists():
#             raise serializers.ValidationError("Email address must be unique.")
#         return value
    
#     def validate_dob(self, value):
#         if value and value > date.today():
#             raise serializers.ValidationError("Date of Birth cannot be in the future.")
#         return value

#     def validate_pin_code(self, value):
#         if len(str(value)) != 6:
#             raise serializers.ValidationError("PIN code must be a 6-digit numeric value.")
#         return value

#     def validate_mobile(self, value):
#         if not value.isdigit() or len(value) != 10:
#             raise serializers.ValidationError("Mobile number must be a 10-digit numeric value.")
#         return value

#     def validate_profession(self, value):
#         if not value.strip():
#             raise serializers.ValidationError("Profession cannot be an empty string.")
#         return value
    
#     def validate_image_size(value):
#         max_size = 5 * 1024 * 1024  # 5 MB
#         if value.size > max_size:
#             raise serializers.ValidationError("Image size must be no more than 5 MB.")
    
#     def validate_image_format(value):
#          valid_formats = ['JPEG', 'PNG']
#          if value.image.format not in valid_formats:
#              raise serializers.ValidationError("Only JPG and PNG formats are supported.")




# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = '__all__'
        
#     def validate_file_field(self, file_field):
#         if not file_field:
#             raise serializers.ValidationError("File field cannot be empty.")
#         return file_field
    


# class ApplicationSerializer(serializers.ModelSerializer):
#     # guarantors = GuarantorSerializer(many=True)
#     # documents = DocumentSerializer()

#     class Meta:
#         model = Application
#         fields = '__all__'
    
#     def validate_aadhaar_no(self, value):
#         if not value.isdigit() or len(value) != 12:
#             raise serializers.ValidationError("Aadhaar number must be a 12-digit numeric value.")
#         return value
    
#     def validate_pan_no(self, value):
#         if not value.isalnum() or len(value) != 12:
#             raise serializers.ValidationError("PAN number must be a 12-character alphanumeric value.")
#         return value

#     def validate_years_in_current_business(self, value):
#         if value < 0:
#             raise serializers.ValidationError("Years in the current business must be a non-negative integer.")
#         return value

#     # def create(self, validated_data):
#     #     guarantors_data = validated_data.pop('guarantors')
#     #     documents_data = validated_data.pop('documents')
#     #     application = Application.objects.create(**validated_data)
#     #     for guarantor_data in guarantors_data:
#     #         Guarantor.objects.create(application=application, **guarantor_data)
#     #         Document.objects.create(application=application, **documents_data)
#     #         return application