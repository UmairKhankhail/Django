from django.shortcuts import render
from .form import StudentRegistration
# Create your views here.

def showdata(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        print(fm)
        if fm.is_valid():

            print("Form Validated.")
            print("Name : ",fm.cleaned_data['name'])
            print("Password : ",fm.cleaned_data['passwd'] )
    else:
        fm=StudentRegistration()
    return render(request,"enroll/form.html",{"form":fm})