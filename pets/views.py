from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import FormularioPets
from .models import Pet
from django.contrib.auth.models import User


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
            formulario.save()
            return redirect('home')
    else:
        form = FormularioPets(request.POST)
    return render(request, 'pets/pet.html', {'form':form})                



    

        


        
        




