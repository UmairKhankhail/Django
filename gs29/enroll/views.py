from django import forms
from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def registration(request):
    fm=StudentRegistration(auto_id='umair_%s',label_suffix='-',initial={'name':'Umair Khan','email':'umiarkhankail@gmail.com'})
    return render(request,'enroll/stu.html',{'form':fm})

