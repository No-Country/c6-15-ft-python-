from urllib import request
from django.shortcuts import render, redirect
from .forms import FormularioPets
from .models import Pet
from django.contrib.auth.models import User


# Create your views here.
def pets(request):
    return render(request, 'homepage/index.html', )

def pets_register(request):
    return render(request, 'pets/pet.html')

# class CreatePet(CreateView):

#     model = Pet
#     form_class = FormularioPets
#     # template_name = 'pets/pet.html'
#     success_message = 'Successfully created post'
#     success_url = reverse_lazy('homepage/index.html')

def createPet(request,user):
    
    if request.method == 'POST':
        form = FormularioPets(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.petowner_id = user
            formulario.save()
            return redirect('home')
    else:
        form = FormularioPets(request.POST)
    return render(request, 'pets/pet.html', {'form':form})                



    

        


        
        



       
        
