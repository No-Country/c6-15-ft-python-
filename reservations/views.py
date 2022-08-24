from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect

from sitter.views import sitter
from .forms import ReservationsForm
from django.contrib.auth.models import User
from sitter.models import Sitter


# Create your views here.
def create_reservation(request, id):
    if request.user.is_authenticated:
        form = ReservationsForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            id = Sitter.objects.get(id = id) 
            formulario.sitter_publication =  id #refrencia al id de publicacion de sitter
            form.save()
            return redirect('home')
        
        context ={
            'form':form
        }
        return render(request, 'reservation.html', context)
    else:
        return render(request, 'reservation.html')
    