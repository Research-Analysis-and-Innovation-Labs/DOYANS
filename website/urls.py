from django.urls import path
from django.urls import include,reverse

# import views
# import views from website\views.py
from . import views

urlpatterns = [
    # pages
    # index
    path('', views.index, name='index'),
]