from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login


# Create your views here.

def login_doggy(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'login.html', {})

    