from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.login_doggy, name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_doggy,name='logout'),
]