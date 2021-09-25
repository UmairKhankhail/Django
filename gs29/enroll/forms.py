from django import forms
from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()