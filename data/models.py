from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.
 

class Product(models.Model):
    sku = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=220)
    date =  models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

class Purchase(models.Model):
    invoice = models.CharField(max_length=15,primary_key=True)
    product = models.ManyToManyField(Product)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True)
    salesman = models.ForeignKey(User,on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.total_price = self.price * self.quantity
        super.save(*args,**kwargs)

    def __str__(self) -> str:
        return f"{self.quantity} of {self.product.name} for {self.total_price}"


########


CATEGORY = (
    ('S', 'Shirt'),
    ('SP', 'Sport Wear'),
    ('OW', 'Out Wear')
)

LABEL = (
    ('N', 'New'),
    ('BS', 'Best Seller')
)

class Item(models.Model) :
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=2)
    label = models.CharField(choices=LABEL, max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            "pk" : self.pk
        
        })

    def get_add_to_cart_url(self) :
        return reverse("core:add-to-cart", kwargs={
            "pk" : self.pk
        })

    def get_remove_from_cart_url(self) :
        return reverse("core:remove-from-cart", kwargs={
            "pk" : self.pk
        })
class OrderItem(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"
class Order(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username