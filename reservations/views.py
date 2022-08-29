from django.shortcuts import render, redirect, get_object_or_404
from sitter.views import sitter
from .forms import ReservationsForm
from django.contrib.auth.models import User
from sitter.models import Sitter
from reservations.models import Reservations
from helpers.send_email import send_email


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
            if form.save():
                email_id = id.user_id.email
                send_email(request,email_id)
                print(email_id)



            list_reservations_id = Reservations.objects.values('id')
            lista = []
            for elem in reversed(list_reservations_id):      
                for k,v in elem.items(): 
                    lista.append(v)
                    if len(lista) == 1:
                        break
            
            return redirect('detail_reservation', lista[0])
        
        context ={
            'form':form
        }
        return render(request, 'reservation.html', context)
    else:
        return render(request, 'reservation.html')
    


#vista para mostrar detalles de la reservacion 

def detail_reservation(request, id):
    if request.user.is_authenticated:
        detail = get_object_or_404(Reservations, id = id)
        return render(request, 'reservations_detail.html', {'detail':detail})


                
