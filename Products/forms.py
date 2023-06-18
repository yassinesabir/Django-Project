from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError


class GestionProduits(forms.Form):
    Name=forms.CharField(label='name')
    email1 = forms.EmailField(label="Adresse e-mail 1")
    email2 = forms.EmailField(label="Adresse e-mail 2")
    def clean(self): 
        cleaned_data = self.cleaned_data
        email1 = self.cleaned_data.get("email1")
        email2 = self.cleaned_data.get("email2")
        if email1.endswith("gmail.com"):
            self.add_error('email1', 'Adresse gmail non acceptée')
        if email2.endswith("gmail.com"):
            self.add_error('email2', 'Adresse gmail non acceptée')
        if email1!=email2:
            raise forms.ValidationError("Les adresses e-mail doivent correspondre.")
        return cleaned_data
