from django.urls import path
from fees import views

urlpatterns=[
    path('django/',views.fees_django),
    path('python/',views.fees_python),
]