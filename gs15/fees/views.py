from django.shortcuts import render

# Create your views here.

def fees_django(request):
    return render(request,'fees/feesone.html',{'title':'Django Fees','fee':'Rs. 5000/=','duration':'5 Months'})