from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import  messages
from django.urls import reverse_lazy
from .forms import RegisterForm, PwdChangingForm, ProfileForm
from django.views import generic
from useraccount.models import Profile

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
  

class UserEditView(generic.UpdateView):
   # form_class = UserChangeForm
    template_name = 'registration/editpro.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('home')
    
    def get_object(self):
      return self.request.user


class UserEditExtendedView(generic.UpdateView):
    model= Profile
    template_name = 'registration/editprofile.html'
    fields = ['street', 'city', 'zip', 'country','stars_average','photo']
    success_url = reverse_lazy('home')
    
        
class PwdChangeView(PasswordChangeView):
    form_class = PwdChangingForm
    success_url = reverse_lazy('password_success')
  
def password_success(request):
    return render(request, 'registration/password_success.html',{})

def create_profile(request,user):
    if request.user.is_authenticated:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            formulario = form.save(commit=False)
            user = User.objects.get(username = request.user.username)
            formulario.user_id = user
            form.save()
            return redirect('home')
        context = {
            'form': form,
        }
   
        return render(request, 'registration/profile.html', context)
    else:
        return render(request, 'profile.html')  
      
