from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:id>', views.create_reservation, name='create_reservation'),
    path('details/<int:id>', views.detail_reservation, name='detail_reservation'),

    ]