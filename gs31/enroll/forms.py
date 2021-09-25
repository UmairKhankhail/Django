from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(initial="Umair Khankhail",help_text="This field initially contain a value which is Umair Khankhail.")
    email=forms.EmailField()
   