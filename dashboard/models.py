from django.db import models

# Create your models here.

class FetchTodayData(models.Model):
    date = models.CharField(max_length=10)
    # time = models.TimeField("Time")
    # temperature = models.FloatField("Temperature")

