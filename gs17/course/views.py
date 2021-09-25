from django.shortcuts import render

# Create your views here.

def learn_django(request):
    return render(request,'course/courseone.html',context={'title':'Learn Django','Course':'Django','duration': '4 Months'})