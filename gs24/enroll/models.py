from django.db import models

# Create your models here.
class Student(models.Model):
    stuname=models.CharField(max_length=40)
    studep=models.CharField(max_length=40)
    stupass=models.CharField(max_length=40)
    stuemail=models.EmailField(max_length=40)