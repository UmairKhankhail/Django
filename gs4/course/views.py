from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("Hello Django Learners!")

def learn_math(request):
    a=2+2
    return HttpResponse(f"2 + 2 = {a}")

def home(request):
    return HttpResponse('about.html')