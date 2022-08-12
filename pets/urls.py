from django.urls import path, include
from . import views

urlpatterns = [
    path('pets',views.pets, name='pets'),
]