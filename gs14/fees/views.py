from django.shortcuts import render

# Create your views here.

def fees_django(request):
    info={'name':"Django Fees Department!"}
    return render(request,'course/info.html',context=info)