from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email_help, name='send_email_help'), ]
