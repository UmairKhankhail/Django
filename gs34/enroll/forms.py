from django import forms
from django.forms import widgets
from django.forms.widgets import Widget

class StudentRegistration(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    hidden=forms.CharField(widget=forms.HiddenInput())
    textarea=forms.CharField(widget=forms.Textarea())
    File=forms.CharField(widget=forms.FileInput)
    classfield=forms.CharField(widget=forms.TextInput(attrs={'class':'somecssone','id':'someunique_id'}))