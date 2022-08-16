from django.urls import path, include
from . import views

urlpatterns = [
    path('pets/',views.pets, name='pets'),
    path('registro_pet/',views.CreatePet.as_view(), name='pets'),
]

