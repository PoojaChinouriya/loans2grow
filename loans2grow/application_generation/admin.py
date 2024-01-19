from django.contrib import admin
from .models import Application, Document, Guarantor
# Register your models here.
admin.site.register(Application)
admin.site.register(Document)
admin.site.register(Guarantor)