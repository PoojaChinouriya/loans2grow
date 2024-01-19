from django.contrib import admin
from .models import Defaulter, Installment, Disbursement

# Register your models here.
admin.site.register(Defaulter)
admin.site.register(Installment)
admin.site.register(Disbursement)
