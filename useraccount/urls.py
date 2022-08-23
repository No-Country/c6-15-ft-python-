from django.urls import path, include
from .views import UserEditView, PwdChangeView, UserEditExtendedView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login',views.login_doggy, name='login'),
    path('register',views.register,name='register'),
    path('<int:pk>', views.assign_role, name='assign_role'),
    path('logout',views.logout_doggy,name='logout'),
    path('editpro', UserEditView.as_view(), name='editpro'),
    path('password', PwdChangeView.as_view(template_name='registration/password.html'), name='password'),
    path('password_success', views.password_success, name='password_success'),
    path('editprofile/<int:pk>/', UserEditExtendedView.as_view(), name='editprofile'), 
   # path('create_profile', views.create_profile, name='create_profile'),
]

app_name = 'useraccount'