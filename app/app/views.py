from django.http import HttpResponse
import datetime

from django.shortcuts import render

def home_page(request):
    current_date = datetime.datetime.now()
    head = "<h1>Welcome to Home Page <br>Current time is {0}</h1>".format(current_date)
    if request.method == 'POST':
        res = request.POST['check']
        print(res)
    return render(request , "home.html",{})

def about(request):
    current_date = datetime.datetime.now()
    head = "<h1>Current time is {0}</h1>".format(current_date)
    return render(request , "about.html",{})
