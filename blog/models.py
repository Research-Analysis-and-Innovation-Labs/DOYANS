from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

# blogs section
class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField(default=None)
    body=models.TextField(null=True)
    # image=models.ImageField(upload_to='blog/img/')
    rating=models.IntegerField(default=0, validators=[MinLengthValidator(0), MaxLengthValidator(5)])
    # authors --> manby to many relationship
    # author=models.ManyToManyField('Author')
    is_bestselling=models.BooleanField(default=False)
    is_featured=models.BooleanField(default=False)

    def __str__(self):
        return self.title

# author
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    # book=models.ManyToManyField('Blog')

    def __str__(self):
        return self.name
