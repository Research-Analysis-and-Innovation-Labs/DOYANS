from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotAllowed,HttpResponseNotFound,HttpResponseRedirect

# Create your views here.

# index view --> main page	
def index(request):
    return render(request, 'website/index.html')