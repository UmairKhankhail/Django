from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(label='YOUR NAME',label_suffix=' - ', initial="Initial Name.",required=False,help_text="70 Character can be written.")
