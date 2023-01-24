from django import forms

from .models import Professor

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Professor
        exclude = []