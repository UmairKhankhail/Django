"""gs7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include

from fees import views as fe
from course import views as cr


urlpatterns = [
    path('admin/', admin.site.urls),

   #This seperates the code but is not independent.

    path('fees/',include([
        path('django/',fe.fees_django),
        path('python/',fe.fees_python),
        ])),
    
    path('course/',include([
        path('django/',cr.learn_django),
        path('python/',cr.learn_python),
    ]))
]
