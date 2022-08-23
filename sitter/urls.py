from django.urls import path, include
from . import views



urlpatterns = [
    path('<str:user>', views.create_sitter, name='create_sitter'),
    path('find_publication/',views.sitter, name='sitter_list'),
]