from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("Hell Django Learners! I am view of fees application.")