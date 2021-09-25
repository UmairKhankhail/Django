from django.shortcuts import render
from datetime import datetime
# Create your views here.

def learn_django(request):
    d=datetime.now()
    data={'nm':'hello learn django!','dt':d,'cm':True,'dj':"Django",'names':['Umair Khankhail','Ulas Yaar','Shahabuddin Khan', 'Muzaffar Ali']}
    return render(request,'course/courseone.html',data)