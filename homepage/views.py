from django.shortcuts import render,redirect
from pets.models import  Pet
from sitter.models import Sitter
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    
    user_role = "(Invitado)"
    
    result_set = Sitter.objects.filter(user_id=request.user.id)
    if result_set:
        user_role = "(Cuidador)"
    
    result_set = Pet.objects.filter(user_id=request.user.id) 
    if result_set:
        user_role = "(Dueño de mascota)"   
        
    return render(request, 'homepage/index.html', {'role': user_role })


