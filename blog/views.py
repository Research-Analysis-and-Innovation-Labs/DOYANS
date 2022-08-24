from django.shortcuts import render
from datetime import date

# Create your views here.
# homepage
def index(request):
    return render(request, "blog/index.html")

# post page
def posts(request):
    return render(request, 'blog/all-posts.html')

# post informations
def post_details(request,slug):
    return render(request, 'blog/post-details.html')