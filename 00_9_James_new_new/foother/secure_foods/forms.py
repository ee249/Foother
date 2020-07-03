from django import forms
from .models import AuthCountry

class AuthCountryForm(forms.ModelForm):
    class Meta:
        model = AuthCountry