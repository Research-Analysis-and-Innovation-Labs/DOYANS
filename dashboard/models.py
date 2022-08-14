from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# user
class User(AbstractUser):
    pass

# user profile
class UserProfile(models.Model):

    # choices
    # gender choices
    gender_choices = (
        ('Male','Male'),('Female','Female'),('Transgender','Transgender')    
    )

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250,null=True)
    # phone = models.IntegerField(max_length=10,null=True)
    gender = models.CharField(gender_choices, max_length=10,null=True)
    public_profile =models.BooleanField(default=False,null=True)
    # files for user profile
    profile_picture=models.ImageField(upload_to='user_profile_pictures/', blank=True, null=True)
    resume = models.FileField(upload_to='user_resume/',blank=True, null=True)
    # manager details,every user has one manager
    manager = models.ForeignKey('UserManager', on_delete=models.CASCADE, related_name='manager', null=True)

    def __str__(self):
        return self.user.name, self.last_name

# user manager
class UserManager(models.Model):
    # manager for user profile, every user has one manager
    user_profile = models.ForeignKey("UserProfile", on_delete=models.CASCADE,null=True,blank=True)
