from django import forms

from .models import Student

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []