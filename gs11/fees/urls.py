from django.urls import path
from fees import views

urlpatterns=[
    path('django/',views.django_fees),
    path('python/',views.python_fees),
]