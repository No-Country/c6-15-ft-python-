from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_reservation, name='create_reservation'),
]