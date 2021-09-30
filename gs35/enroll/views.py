from django.shortcuts import render
from .forms import studentRegistration
# Create your views here.

def studentregistration(request):
    fm=studentRegistration()
    return render(request,'enroll/forms.html',{'forms':fm})