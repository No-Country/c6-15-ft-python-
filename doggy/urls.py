"""doggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from homepage import urls
from useraccount import urls
from sitter import urls

=======
from pets import urls
>>>>>>> 2ff247a7b6482cbe7ecb74143703612e06c3cd6a

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('pets/', include('pets.urls')),
    path('useraccount/', include('useraccount.urls')),
<<<<<<< HEAD
    path('sitter/', include('sitter.urls')),

=======
>>>>>>> 2ff247a7b6482cbe7ecb74143703612e06c3cd6a
]
