from django.urls import path
from . import views

urlpatterns = [
    path('django/',views.fees_django),
]
