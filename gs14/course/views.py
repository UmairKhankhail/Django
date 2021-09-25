from django.shortcuts import render

# Create your views here.

def learn_django(request):
    info={'name':"Django"}
    return render(request,'course/info.html',context=info)