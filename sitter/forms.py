from random import choices
from django import forms
from sitter.models import Sitter
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

numeric = RegexValidator(r'^[0-9+]', 'Only digit characters.')

def validate_even(value):
    if not(value >0):
        raise ValidationError(
            _('%(value)s No es un número válido'),
            params={'value': value},
        )

status_pub = [
    (1, 'Activa'),
    (2, 'Inactiva'),
]

class SitterForm(forms.ModelForm):
  
       
    
    price = forms.IntegerField(label='Precio', initial=100, required=False, validators=[validate_even],
                             widget=forms.NumberInput(attrs={'class': 'form-control','required':'True'}))
    descripcion = forms.CharField(label='Descripcion',required=False,max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='Status', choices=status_pub,required=False)
    
    picture_site = forms.ImageField(label='Subir Foto',required=True,
                                    widget=forms.FileInput(attrs={'required':'True','help_text':'Campo requierido'}))
    
                                    

    class Meta:
        model = Sitter
        fields = ['price', 'descripcion', 'status', 'picture_site','user_id']
        exclude = ['user_id']
    
    
          
       
            
        
