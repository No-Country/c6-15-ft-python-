from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Reservations

class ReservationsForm(forms.ModelForm):


    class Meta:
        model = Reservations
        fields = ['check_in', 'check_out', 'payment_type']


        widgets = {

            'check_in': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Check In', 'type': 'date'}),
            'check_out': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Check Out', 'type': 'date'})

        }