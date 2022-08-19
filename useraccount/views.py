from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import  messages
from .forms import RegisterForm

# Create your views here.

def login_doggy(request):
    if request.user.is_authenticated:
        messages.error(request,'Ya estas logeado ')
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            messages.success(request,'Bienvenido de nuevo {}'.format(user.username))
            return redirect('home')

        else:
            messages.error(request,'Usuario o contraseña no validos')
        
    return render(request,'login.html', {})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request,user)
            messages.success(request,'Cuenta creada exitosamente')
            return redirect('home')

    return render(request,'register.html',{
        'form' : form,
    })

def logout_doggy(request):
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    messages.success(request,'Salió de sesión exitosamente')
    return redirect('home')