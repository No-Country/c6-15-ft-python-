from django.urls import path, include
from . import views
urlpatterns = [
    path('login',views.login_doggy, name='login'),
    path('register',views.register,name='register'),
    path('logoute',views.logout_doggy,name='logout'),
    path('edit_profile',views.edit_profile, name='edit_profile'),
]