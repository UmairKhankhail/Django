from django.urls.conf import path
from course import views

urlpatterns=[
    path('learndj/',views.learn_django),
    path('learnm/',views.learn_math),
]