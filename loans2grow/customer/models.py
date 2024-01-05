from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Enquiry(models.Model):
    ENQUIRY_STATUS = [
        ('pending','pending'),
        ('done','done'),
        ('rejected','rejected'),
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = PhoneNumberField(region='IN')
    message = models.TextField()
    enquiry_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    status = models.CharField(max_length=10, choices=ENQUIRY_STATUS)
    response_timestamp = models.DateTimeField(blank=True, null=True)
