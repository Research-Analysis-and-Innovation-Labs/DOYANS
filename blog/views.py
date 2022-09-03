from logging import raiseExceptions
from datetime import date
from urllib import request

from django.shortcuts import render,get_object_or_404 # get object or 404 error
from django.http import Http404 # return http 404 pages
from django.db.models import Avg,Max,Min # import aggregate class
from django.http import HttpResponseRedirect # redirection
from .models import Blog

# Create your views here.
# homepage
def index(request):
    return render(request, "blog/index.html")

# post page
def posts(request):
    # save query in cache variable --> to prevent database overuse, hit database only once
    post=Blog.objects.all().order_by('-title') # get all posts and order by title in descending prder
    # aggregation
    post_count=post.count()
    post_average_rating=post.aggregate(Avg("rating")) # take rating average
    post_minimum_rating=post.aggregate(Min("rating")) # rating mimimum values
    latest_posts=sorted(post[:3])
    return render(request, 'blog/posts.html',{
        # post aggregate details
        'post':latest_posts,
        'total_posts':post_count,
        'average_rating': post_average_rating,
        'minimum_rating': post_minimum_rating,
    })

# post details
def post_details(request,slug):
    # save query in cache variable --> to prevent database overuse, hit database only once
    post=get_object_or_404(Blog,slug=slug) # get posts by slugs or 404

    return render(request, 'blog/post-details.html',{
        # post details
        "title":post.title,
        "body":post.body,
        "rating":post.rating,
        "is_bestselling":post.is_bestselling,
        "is_featured":post.is_featured,
    })


# formpage
def forms(request):
    # if method of request is POST
    if request.method=='POST':
        # set a variable to value to POST key with name=form
        information=request.POST['form']
        # return url path of /form-end page through .urls
        return HttpResponseRedirect("form-end") # redirect to same application page

    # return hr form page
    return render(request,"blog/form.html")

# form end page
def form_ending(request):
    return render(request,"blog/form_ending.html")