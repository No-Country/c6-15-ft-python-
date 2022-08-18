from django.shortcuts import render
from sitter.forms import SitterForm
from django.contrib.auth.models import User
# Create your views here.


def create_sitter(request,user):
    if request.user.is_authenticated:
        form = SitterForm(request.POST or None)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            form.save()
        context = {
            'form': form,
        }
        print(form)
        return render(request, 'sitter.html', context)
    else:
        return render(request, 'sitter.html')