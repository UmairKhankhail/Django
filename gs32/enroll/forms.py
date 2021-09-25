from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    id=forms.IntegerField()
    key=forms.CharField(widget=forms.HiddenInput())