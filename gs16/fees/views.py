from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request,'fees/feesone.html',context={'title':'Django Fees','course':'Django','amount':'Rs. 5000/='})