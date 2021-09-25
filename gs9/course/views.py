from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("<h1>hello django</h1>")


def learn_python(request):
    return HttpResponse("<h1>hello pyhton</h1>")