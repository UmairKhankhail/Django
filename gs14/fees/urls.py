from django.urls import path
from fees import views

urlpatterns=[
    path('django/',views.fees_django),
]