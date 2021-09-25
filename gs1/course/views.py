from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("<h1>Hello Django</h1>")