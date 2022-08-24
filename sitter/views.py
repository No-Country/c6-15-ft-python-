from django.shortcuts import render, redirect, get_object_or_404
from sitter.forms import SitterForm
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Sitter
from .forms import SitterForm
from django.urls import reverse_lazy
# Create your views here.


def create_sitter(request,user):
    if request.user.is_authenticated:
        form = SitterForm(request.POST, request.FILES)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            form.save()
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

def sitter_details(request, pk):
    if request.user.is_authenticated:
        details = get_object_or_404(Sitter, id=pk)
        print(details)
        
    return render(request, 'sitter_detail.html', {'details':details})