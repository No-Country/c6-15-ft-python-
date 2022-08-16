from django import forms
from .models import Pet

class FormularioPets(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ['name','age','size','condition', 'accesories']
        widgets = {
            'age': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'edad',
                }
            ),
            'size': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'tamaño',
                }
            ),
            'condition': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'condiciones',
                }
            ),
            'accesories': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'accesorios',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'nombre',
                }
            ),
        }

