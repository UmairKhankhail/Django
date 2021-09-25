from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=80)
    password=models.CharField(max_length=70)
    address=models.CharField( max_length=50)

    def __str__(self):
        return self.name
    