from django.contrib import admin

from .models import Statistic

# configure admin site
# statistics
class StatisticAdmin(admin.ModelAdmin):
    prepopulated_fields: {'slug': ("name",)}
    list_filter: ('name','grade',)
    list_display: ('name','grade',)


# Register your models here.
# statistics
admin.site.register(Statistic,StatisticAdmin) # statistics admin configuration