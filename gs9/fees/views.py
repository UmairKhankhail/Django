from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def fees_django(request):
    return render(request,'feesone.html')

def fees_python(request):
    return render(request,'feestwo.html')