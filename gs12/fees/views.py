from django.shortcuts import render

# Create your views here.

def django_fees(request):
    dic1={'fname':'Django','ffee':5000}
    return render(request,'fees/feesone.html',context=dic1)

def python_fees(request):
    dic2={'fname':'Python','ffee':3000}
    return render(request,'fees/feestwo.html',context=dic2)