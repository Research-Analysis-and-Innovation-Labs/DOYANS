# classes to save information in database

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator # validators for fields
from django.urls import reverse
from django.utils.text import slugify # slug conversion


## Create your models here.

# publisher
class Publisher(models.Model):
    name=models.CharField(max_length=100)
    business_name=models.CharField(max_length=100)
    code=models.IntegerField()


    def __str__(self) -> str:
        return self.name


# address 
class Address(models.Model):
    area=models.CharField(max_length=100)
    road=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()

    def full_address(self):
        return f"{self.area}.{self.road}.{self.city}.{self.zipcode}"

    def __str__(self):
        return self.city

    # meta class configurations and behaviours --> rename table name in admin dashboard
    class Meta:
        verbose_name_plural="Author Address"

# author
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    address=models.TextField(max_length=250,blank=True)
    is_bestseller=models.BooleanField(default=False)
    slug=models.SlugField(null=False, db_index=True) # slug field
    # address - one to one relationship
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True) # on delete remove data

    # full name(
    def fullname(self):
        return self.name

    # url for models
    def get_absolute_url(self):
        return reverse("author-detail", args=[self.slug])
    
    # modify exsiting function --> save()
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    # return string representation of function in 
    def __str__(self):
        return self.fullname()

# inventory
class Inventory(models.Model):
    warehouse=models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural="Inventory"
    

    def __str__(self):
        return self.warehouse


# blog categories
class BlogCategory(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural="Blog Catgeories" 

    def __str__(self) -> str:
        return self.name

# blog tags
class BlogTag(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural="Blog Tags" 

    def __str__(self) -> str:
        return self.name

# blogs
class Blog(models.Model):
    title=models.CharField(max_length=100) # max_length necessary for - charfields
    pub_date=models.DateTimeField(auto_now_add=True,blank=True) # automataiccly saves to publication date
    last_modified=models.DateTimeField(auto_now=True,null=True) # automaticaly saves to last saved
    body=models.TextField(blank=True,null=True)
    # rating=models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    source=models.URLField(null=True)
    is_bestselling=models.BooleanField(default=False)
    is_featured=models.BooleanField(default=False)
    slug=models.SlugField(null=False, db_index=True, unique=True) # slug field
    # author - foreign keys <--> one to may relationship
    author=models.ForeignKey(Author,blank=True,on_delete=models.SET_NULL,null=True,related_name='blogs') # on delete set null
    # inventory - one to one relationhip
    inventory=models.OneToOneField(Inventory,on_delete=models.SET_NULL,null=True)
    # publisher - one to many relationship, no need for on_delete
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE,null=True,related_name='blogs')
    # category - one to many
    category=models.ForeignKey(BlogCategory,on_delete=models.SET_NULL,null=True)
    # tags - many to many
    tags=models.ManyToManyField(BlogTag)


    # url for models
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    # modify exsiting function --> save()
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    # return string representation of function in 
    def __str__(self):
        return self.title

    

