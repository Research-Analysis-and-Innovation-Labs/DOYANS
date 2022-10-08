# path address and map with funcitons,classes in views.py

from django.urls import path
from django.urls import include,reverse

# import views
# import views from blog\views.py
from . import views

urlpatterns = [
    # pages
    # index
    path('', views.index, name='index'),
    # posts
    path('posts', views.posts, name='posts'),
    # post details
    path('<int:id>', views.post_details, name='post-details'),
    # form page
    path("form",views.forms,name="forms"),
    # form ending page
    path("form-end",views.form_ending,name="form_ending")
]