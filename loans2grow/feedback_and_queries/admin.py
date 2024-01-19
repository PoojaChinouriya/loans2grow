from django.contrib import admin
from feedback_and_queries.models import FAQ, FeedBack, Queries

# Register your models here.
admin.site.register(FAQ)
admin.site.register(FeedBack)
admin.site.register(Queries)