from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def djnango_fee(request):
    return HttpResponse('500')


def python_fee(request):
    return HttpResponse('300')
    