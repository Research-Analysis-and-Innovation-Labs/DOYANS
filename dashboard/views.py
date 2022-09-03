from django.shortcuts import render, redirect
from django.http import Http404,HttpResponse,HttpResponseNotAllowed,HttpResponseNotFound,HttpResponseRedirect

from .models import Statistic

# Create your views here.

# 404 error page
def error_message(request):
    return render(request, 'dashboard/error/404.html')

# index view --> main page
def index(request):
    return render(request, "dashboard/index.html")


# metrics view --> metrics and analytics page
def metrics(request):
    return render(request, 'dashboard/data/metrics.html')

# user_query view --> user query and take action -> <user_query>
def user_query(request, user_query):
    # dictionary for user query input
    user_query_options={
        'hi': 'hi',
        'hello': 'hello',
        'bye': 'bye',
        'goodbye': 'goodbye',
        'thanks': 'thanks'
        }
    # for strings query
    if type(user_query) == str:
        try:
            output=user_query_options[user_query]
            return render(request, 'dashboard/data/query.html', {'output': output})
        except:
            return render(request, 'dashboard/error/404.html')
        # return render(request, 'dashboard/user_query.html')
    # for integers query
    elif type(user_query) == int:
        if user_query<len(list(user_query_options.keys())):
            try:
                output=list(user_query_options.keys())[user_query-1]
                return redirect(request, 'dashboard/query.html', {'output': output})
            except:
                return render(request, 'dashboard/error/404.html')
        else:
            return render(request, 'dashboard/error/404.html')