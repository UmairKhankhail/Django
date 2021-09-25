from django.db import models
from django.db.models.lookups import Contains

# Create your models here.
class Student(models.Model):
    stu_roll=models.IntegerField()
    stu_name=models.CharField(max_length=40)
    stu_dep=models.CharField(max_length=40)
    stu_email=models.EmailField(max_length=20)
    stu_pass=models.CharField(max_length=15)

    def __str__(self):
       return self.stu_name

class Teacher(models.Model):
    t_roll=models.IntegerField()
    t_name=models.CharField(max_length=50)
    t_dep=models.CharField(max_length=50)
    t_email=models.EmailField(max_length=40)

    def __str__(self):
        return str(self.t_roll)
    