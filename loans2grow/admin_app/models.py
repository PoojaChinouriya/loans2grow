from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .manager import CustomUserManager


class User(AbstractUser):
    GENDER_CHOICES = [
        ('male','male'),
        ('female','female'),
        ('transgender','transgender'),
    ]
    ROLE_CHOICES = [
        ('customer','customer'),
        ('loan_representative','loan_representative'),
        ('operational_head','operational_head'),
        ('loan_sanctioning_officer','loan_sanctioning_officer'),
        ('admin','admin'),
        ('account_head','account_head'),
    ]
    dob = models.DateField(blank=True, default='2000-12-12')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    permanent_address = models.TextField(blank=True, null=True)
    current_address = models.TextField(blank=True, null=True)
    mobile = PhoneNumberField(region='IN', blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='photo/', null=True)
    signature = models.ImageField(blank=True, upload_to='signature/', null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name','last_name','mobile')

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Family(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('married','married'),
        ('unmarried','unmarried'),
        ('divorced','divorced'),
    ]

    user = models.OneToOneField('admin_app.User', on_delete=models.CASCADE, related_name='family')
    father_name = models.CharField(max_length=30, blank=True, default='')
    father_profession = models.CharField(max_length=30, blank=True, default='')
    father_income = models.FloatField(blank=True, default=0.0)
    father_contact = PhoneNumberField(region='IN',blank=True, null=True)
    mother_name = models.CharField(max_length=30, blank=True, default='')
    mother_profession = models.CharField(max_length=30, blank=True, default='')
    mother_income = models.FloatField(blank=True, default=0.0)
    mother_contact = PhoneNumberField(region='IN',blank=True, null=True)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES, default='Unmarried')
    spouse_name = models.CharField(max_length=20, default='', blank=True)
    spouse_income = models.FloatField(blank=True, default=0.0)
    spouse_profession = models.CharField(max_length=30, default='', blank=True)
    spouse_contact = PhoneNumberField(region='IN',blank=True, null=True)


class Bank(models.Model):
    user = models.ForeignKey('admin_app.User', on_delete=models.CASCADE, related_name='banks')
    bank_name = models.CharField(max_length=30, default='', blank=True, null=True )
    account_number = models.CharField(max_length=20, default='', blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, default='', blank=True)
    passbook_copy = models.ImageField(upload_to='customer/bank/', blank=True, null=True)
    bank_address = models.TextField(blank=True, null=True) 

