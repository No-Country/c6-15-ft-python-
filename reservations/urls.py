from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:id>', views.create_reservation, name='create_reservation'),
]