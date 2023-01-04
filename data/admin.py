from django.contrib import admin

# import modules

from .models import (
    Product,Purchase,
    Item,OrderItem,Order,
)

# Register your models here.

admin.site.register(Product)
admin.site.register(Purchase)

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)