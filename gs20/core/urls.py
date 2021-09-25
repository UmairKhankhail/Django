from django.urls import path
from core import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
]
