from django.contrib import admin
from .models import Defaulter, Disbursement, Installment

# Register your models here.
admin.site.register(Disbursement)
admin.site.register(Defaulter)
admin.site.register(Installment)
