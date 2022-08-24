from django.urls import path
from django.urls import include,reverse

# import views
# import views from dashboard\views.py
from . import views

urlpatterns = [
    # pages
    # index
    path('', views.index, name='index'),
    # metrics
    path('data', views.metrics, name='metrics'),

    # queries
    # user query and take action -> <user_query>
    path('<user_query>', views.user_query, name='user_query'),


]
