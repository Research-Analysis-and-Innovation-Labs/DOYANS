from django.contrib import admin

# applications
from dashboard import models as dashboard_models

# Register your models here.
admin.site.register(dashboard_models.FetchTodayData)