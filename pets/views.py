from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import FormularioPets
from .models import Pet
from sitter.models import Sitter
from sitter.forms import SitterForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def pets(request):
    return render(request, 'homepage/index.html', )

def pets_register(request):
    return render(request, 'pets/pet.html')



def createPet(request,user):
    
    
    if request.method == 'POST':

        form = FormularioPets(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            if not is_sitter(formulario.user_id):
                formulario.save()
                messages.success(request,'En hora buena!, registraste a doggy correctamente.')  
                return redirect('home')
            else:
                messages.error(request,'Acción no permitida: Anteriormente te registraste como cuidador')  
                return redirect('home')
                
    else:
        
        form = FormularioPets()
    return render(request, 'pets/pet.html', {'form':form})                

def is_sitter(user_identification):
    return Sitter.objects.filter(user_id=user_identification)


   
            

    

        


        
        




