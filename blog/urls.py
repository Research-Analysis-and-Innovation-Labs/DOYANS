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
    path('post/<slug:slug>', views.post_details, name='post-details'),
]