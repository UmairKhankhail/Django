from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def learn_django(request):
   return HttpResponse("Hello Django")


def learn_math(request):
    return HttpResponse("This is mathematics class, so please listen carefully.")