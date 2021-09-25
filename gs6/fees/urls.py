from django.urls import path
from . import views

urlpatterns=[
    path('python_fee/',views.python_fee),
    path('django_fee/',views.djnango_fee),
]