from django.urls import path
from . import views



urlpatterns = [
    path('<str:user>', views.create_sitter, name='create_sitter'),
    path('find_publication/',views.sitter, name='sitter_list'),
    path('sitter_details/<int:id>', views.sitter_details, name='sitter_details')
]