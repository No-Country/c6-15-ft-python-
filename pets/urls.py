from django.urls import path, include
from . import views

app_name = 'pet'



urlpatterns = [
    path('pets/',views.pets, name='pets'),
    # path('registro_pet/<int:user_id>',views.CreatePet.as_view(), name='pets_register'),
    path('registro_pett/<str:user>/',views.createPet, name='register'),
    

]


