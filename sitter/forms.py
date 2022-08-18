from telnetlib import STATUS
from django import forms
from sitter.models import Sitter


class SitterForm(forms.ModelForm):
    
    class Meta:
        model = Sitter
        fields = ['price', 'descripcion', 'status', 'picture_site']


        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'picture_site': forms.FileInput(attrs={'class': 'form-control'}),
        }

    