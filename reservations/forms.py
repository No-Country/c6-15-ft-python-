from dataclasses import fields
from datetime import datetime
from django import forms
from .models import Reservations
from datetime import date

today = date.today()

class ReservationsForm(forms.ModelForm):

     check_in = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': today ,'placeholder': 'Check In', 'type': 'date' }))
     check_out = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': today ,'placeholder': 'Check Out', 'type': 'date' }))
      
     class Meta:
        model = Reservations
        fields = ['check_in', 'check_out', 'payment_type']


