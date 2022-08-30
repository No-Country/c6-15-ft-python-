from django.urls import path, include
from .views import UserEditView, PwdChangeView, UserEditExtendedView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'useraccount'
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login_doggy, name='login'),
    path('password', PwdChangeView.as_view(template_name='registration/password.html'),name='password'),
    path('pwdsuccess', views.pwdsuccess, name='pwdsuccess'),
    path('<int:pk>', views.assign_role, name='assign_role'),
    path('logout',views.logout_doggy,name='logout'),
    path('editpro', UserEditView.as_view(), name='editpro'),

    path('password', PwdChangeView.as_view(template_name='registration/password.html'), name='password'),
<<<<<<< HEAD
<<<<<<< HEAD
    #path('password_success', views.password_success, name='password_success'),
=======
   # path('password_success', views.password_success, name='password_success'),
>>>>>>> Urls
=======
   # path('password_success', views.password_success, name='password_success'),
=======
    #path('password_success', views.password_success, name='password_success'),
>>>>>>> a03a009845ce17178317b58e904f4a09e63bdff1
>>>>>>> 4f106d0f0cd1d9756725aad0a2437addb973991c
    path('editprofile/<int:pk>/', UserEditExtendedView.as_view(), name='editprofile'), 
   # path('create_profile', views.create_profile, name='create_profile'),

    
    
   

]

