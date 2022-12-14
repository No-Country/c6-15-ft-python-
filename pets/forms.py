from importlib.metadata import requires
from django import forms
from .models import Pet

class FormularioPets(forms.ModelForm):
    

    class Meta:
        model = Pet
        fields = ['name','age','size','condition', 'accesories','petowner_id']
        exclude = ['petowner_id']
        
        labels = {
            'name': 'Nombre del perro',
            'age': 'Edad del perro',
            'size': 'Talla del perro',
            'condition': 'Condiciones Especiales',
            'accesories': 'Accesorios',
        }

        

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'nombre',
                   
                }
            ),
            
            'age': forms.NumberInput(
                
                attrs={
                    'class':'form-control',
                    'placeholder':'edad',
                }
            ),
            'size': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'tamaño: chica mediana grande',
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
                    'placeholder':'ej: collar, pelota, correa etc.',
                    
                }
                
            ),

            

        }

            
        
