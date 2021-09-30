from django import forms
from django.forms.widgets import PasswordInput

class StudentRegistration(forms.Form):
    name=forms.CharField()
    passwd=forms.CharField(widget=forms.PasswordInput())
    