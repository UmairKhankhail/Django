from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def student(request):
    fm=StudentRegistration(initial={'name':'Runtime initial value.'})
    fm.order_fields(field_order=(['id','name','email']))
    return render(request,'enroll/stu.html',{'form':fm})

