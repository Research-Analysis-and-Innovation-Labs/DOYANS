# admin dashboard configurations

from ast import Add
from django.contrib import admin

from .models import Blog, Author, Address, BlogCategory, BlogTag, Inventory, Publisher

# admin configuration
# blog admin
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",'author',)}
    # filter section in admin side
    list_filter = ('category','author',)
    # display fields sections in tables
    list_display = ('title','pub_date','author',)

# Register your models here.
# publisher
admin.site.register(Publisher)
# inventory
admin.site.register(Inventory)
# address
admin.site.register(Address)
# author
admin.site.register(Author)

# category
admin.site.register(BlogCategory)

# category
admin.site.register(BlogTag)

# blog
admin.site.register(Blog,BlogAdmin)

