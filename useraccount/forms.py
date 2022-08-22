from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .models import Profile
class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'id' : 'username',
                                    'placeholder' : 'Username'
                                }))
    
    
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                'class' : 'form-control',
                                'id' : 'username',
        '                       placeholder' : 'example@gmail.com',
        }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control',
                                }))
    
    
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email

    def clean_role(self):
        role = self.cleaned_data.get('email')

        return role

    
   
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),

        )

    
class UserChangeForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'id' : 'username',
                                    'placeholder' : 'Username'
                                }))

class PwdChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Password actual',widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1= forms.CharField(label='Password nuevo',max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2= forms.CharField(label='Confirma password',max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
      model = User
      fields = ('old_password', 'new_password1', 'new_password2')  


#class ProfileForm(forms.ModelForm):
 #   class Meta:
  #      model = Profile
   #     fields = ['street', 'zip', 'city', 'country', 'photo']

    #    widgets = {
     #       'street': forms.TextInput(attrs={'class':'form-control','placeholder':'Street'}),
      #      'zip': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
       #     'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            
       # }
        
   

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['street', 'zip', 'city', 'country', 'photo']
        
        labels = {
            'street': 'Domicilio',
            'zip': 'Código Postal',
            'city': 'Ciudad',
            'country': 'País',
            'photo': 'Fotografía',
        }

        

        widgets = {
            'street': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Domicilio',
                }
            ),
            
            'zip': forms.NumberInput(
                
                attrs={
                    'class':'form-control',
                    'placeholder':'Código Postal',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ciudad',
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'País',
                }
            ),
            
        }

