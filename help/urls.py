from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_help, name='user_help'),
    ]