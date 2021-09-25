from django.shortcuts import render

# Create your views here.
def django_fees(request):
    return render(request,'feesone.html')

def python_fees(request):
    return render(request,'feestwo.html')

    