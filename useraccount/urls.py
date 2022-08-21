from django.urls import path, include
from .views import UserEditView, PwdChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login',views.login_doggy, name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_doggy,name='logout'),
    path('editpro', UserEditView.as_view(), name='editpro'),
    path('password', PwdChangeView.as_view(template_name='registration/password.html'), name='password'),
    path('password_success', views.password_success, name='password_success'),
]

app_name = 'useraccount'