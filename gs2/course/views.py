from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h5>Home Page</h5>")

def learn_django(request):
    return HttpResponse("<h2>Hello Django!</h2>")

def learn_python(request):
    return HttpResponse("Hello Python!")

def learn_variable(request):
    a="<h1>I am variable. Hey!</h1>"
    return HttpResponse(a)

def learn_math(request):
    a=20+30
    return HttpResponse(a)

def learn_format(request):
    b="GeekShows"
    return HttpResponse(f"Hello Dear! You are learning from {b}")

