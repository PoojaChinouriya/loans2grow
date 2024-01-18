# from rest_framework import serializers
# from .models import User, Family, Bank



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


# class FamilySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Family
#         fields = '__all__'


# class BankSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bank
#         fields = '__all__'




























#     def validate_email(self, value):
#         if get_user_model().objects.filter(email=value).exists():
#             raise serializers.ValidationError("Email address must be unique.")
#         return value
    
#     def validate_image_size(self, value):
#         max_size = 5 * 1024 * 1024  # 5 MB
#         if value.size > max_size:
#             raise serializers.ValidationError("Image size must be no more than 5 MB.")
    
#     def validate_image_format(self, value):
#          valid_formats = ['JPEG', 'PNG', 'JPG']
#          if value.image.format not in valid_formats:
#              raise serializers.ValidationError("Only JPG and PNG formats are supported.")
         
#     def validate_dob(self, value):
#         from datetime import date
#         if value and value > date.today():
#             raise serializers.ValidationError("Date of Birth cannot be in the future.")
#         return value


# class FamilySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Family
#         fields = '__all__'

# class BankSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bank
#         fields = '__all__'

#     def validate_father_income(self, value):
#         if value < 0:
#             raise serializers.ValidationError("Father's income cannot be negative.")
#         return value

#     def validate_mother_income(self, value):
#         if value < 0:
#             raise serializers.ValidationError("Mother's income cannot be negative.")
#         return value

#     def validate_spouse_income(self, value):
#         if value < 0:
#             raise serializers.ValidationError("Spouse's income cannot be negative.")
#         return value

    



#     def validate_account_number(self, value):
#         if not value:
#             raise serializers.ValidationError("Account number cannot be empty.")
#         return value

#     def validate_ifsc_code(self, value):
#         if not value:
#             raise serializers.ValidationError("IFSC code cannot be empty.")
#         return value
    
#     def validate_image_size(value):
#         max_size = 5 * 1024 * 1024  # 5 MB
#         if value.size > max_size:
#             raise serializers.ValidationError("Image size must be no more than 5 MB.")
    
#     def validate_image_format(value):
#          valid_formats = ['JPEG', 'PNG', 'JPG']
#          if value.image.format not in valid_formats:
#              raise serializers.ValidationError("Only JPG and PNG formats are supported.")


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)
    



