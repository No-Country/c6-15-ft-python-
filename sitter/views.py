from django.shortcuts import render, redirect, get_object_or_404
from sitter.forms import SitterForm
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Sitter
from pets.models import Pet
from .forms import SitterForm
from django.urls import reverse_lazy
from django.contrib import  messages
from useraccount.forms import RegisterForm
# Create your views here.


def create_sitter(request,user):
    if request.user.is_authenticated:
        form = SitterForm(request.POST, request.FILES)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            if not is_petowner(user):
                if is_valid_publication(user):
                    form.save()
                    messages.success(request,'Felicidades!, acabas de anunciarte')  
                    return redirect('home')
                else:
                    messages.error(request,'Acción no permitida: ya cuenta con una publicación')  
                    return redirect('home')
            else:
                messages.error(request,'Acción no permitida: Anteriormente te registraste como dueño de mascota')  
                return redirect('home')    
                    
        context = { 
            'form': form,
        }
   
        return render(request, 'sitter.html', context)
    else:
        return render(request, 'sitter.html')


def sitter(request):
    query = Sitter.objects.filter(status=1)
    return render(request, 'sitter_publications.html', {'query':query})
  
def is_valid_publication(user_name):
    return not Sitter.objects.filter(user_id=user_name)
  
    

def sitter_details(request, id):
    if request.user.is_authenticated:
        details = get_object_or_404(Sitter, id = id) 
    return render(request, 'sitter_detail.html', {'details':details})


<<<<<<< HEAD

def sitter(request):
    query = Sitter.objects.filter(status=1)
    return render(request, 'sitter_publications.html', {'query':query})
  
def is_valid_publication(user_name):
    return not Sitter.objects.filter(user_id=user_name)
  
def is_petowner(user_identification):
    return Pet.objects.filter(user_id=user_identification)
=======
    
>>>>>>> 1642af973b213167f2b234860a1760309ccedd09
