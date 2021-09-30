from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def thankyou(request):
    return render(request,'enroll/sucuss.html')

def showstudentdata(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        print(fm)
        if fm.is_valid():
            print("Form Validated")
            print("Name : ",fm.cleaned_data["name"])
            print("Email : ",fm.cleaned_data["email"])
            print("Password : ",fm.cleaned_data["passwd"])

            return HttpResponseRedirect('/registration/sucuss/')
    else:
        fm=StudentRegistration()

    return render(request,"enroll/form.html",{'form':fm})
