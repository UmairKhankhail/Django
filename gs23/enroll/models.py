from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stufn=models.CharField(max_length=20)
    stuln=models.CharField(max_length=20)
    stupass=models.CharField(max_length=100)
    stuadd=models.CharField(max_length=100, default='not available')
    stuemail=models.EmailField(max_length=50)
