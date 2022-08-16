from django.urls import path
from . import views

urlpatterns = [
    path('sitter/',views.sitter, name='sitter'),
]
