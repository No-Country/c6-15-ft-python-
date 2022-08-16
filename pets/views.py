
from django.shortcuts import render
from .forms import FormularioPets
from django.views.generic import CreateView
from .models import Pet
from django.urls import reverse_lazy

# Create your views here.
def pets(request):
    return render(request, 'homepage/index.html', )

def pets_register(request):
    return render(request, 'pets/pet.html')

class CreatePet(CreateView):

    model = Pet
    form_class = FormularioPets
    template_name = 'pets/pet.html'
    success_url = reverse_lazy('homepage/index.html')

