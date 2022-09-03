from django.db import models
from django.utils.text import slugify # slug conversion
from django.core.validators import MinLengthValidator, MaxLengthValidator # validators for fields


# Create your models here.

class Statistic(models.Model):
    name = models.CharField(max_length=100,blank=True)
    slug=models.SlugField(default="",null=False, db_index=True) # slug field
    information=models.TextField(blank=True)
    grade=models.IntegerField(default=0,blank=True,validators=[MinLengthValidator(0),MaxLengthValidator(10)])


    # def get_absolute_url(self):
    #     return reverse("statistic-details", args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return f"{self.name}"
    

