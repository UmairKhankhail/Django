from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    passwd=forms.CharField(widget=forms.PasswordInput())