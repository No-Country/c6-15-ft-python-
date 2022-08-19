from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>', views.create_sitter, name='create_sitter'),
]