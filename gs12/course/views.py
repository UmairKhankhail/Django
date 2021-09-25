from django.shortcuts import render

# Create your views here.

def learn_django(request):
    cdic1={'cname':'Django','ctime':'4 Months','crequire':'Python'}
    return render(request,'course/courseone.html',cdic1)

def learn_python(request):
    cdic2={'cname':'Python','ctime':'3 Months','crequire':'None'}
    return render(request,'course/coursetwo.html',cdic2)