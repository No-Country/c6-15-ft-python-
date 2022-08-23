from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import ReservationsForm
from django.contrib.auth.models import User


# Create your views here.
def create_reservation(request, pk):
    if request.user.is_authenticated:
        form = ReservationsForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            sitter_id = pk
            print(sitter_id)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            formulario.sitter_publication = sitter_id
            form.save()
            return redirect('index')
        
        context ={
            'form':form
        }
        return render(request, 'reservation.html', context)
    else:
        return render(request, 'reservation.html')
    