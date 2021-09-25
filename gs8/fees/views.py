from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def fees_django(request):
    return HttpResponse(500)

def fees_python(request):
    return HttpResponse(300)
