from django.urls import path
from . import views
urlpatterns = [
    path("student/",views.showstudentdata),
    path('sucuss/',views.thankyou),
]
