from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import ReservationsForm
from django.contrib.auth.models import User


# Create your views here.
def create_reservation(request):
    if request.user.is_authenticated:
        form = ReservationsForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            form.save()
            return redirect('index.html')
        
        context ={
            'form':form
        }
        return render(request, 'reservation.html', context)
    else:
        return render(request, 'reservation.html')
    