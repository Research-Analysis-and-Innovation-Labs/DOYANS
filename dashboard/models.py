from django.db import models

# Create your models here.

class Statistics(models.Model):
    type = models.CharField(max_length=100,default=None,blank=True)
    name = models.CharField(max_length=100, default=None,blank=True)

    def __str__(self) -> str:
        return self.name
