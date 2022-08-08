from enum import unique
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, min_length=3)
    last_name = models.CharField(max_length=100, min_length=3)
    email = models.EmailField(max_length=100, min_length=3, unique=True)
    phone = models.CharField(max_length=10, min_length=7)
    province = models.CharField(max_length=20, min_length=5)
    city = models.CharField(max_length=50, min_length=2)
    adress_street = models.CharField(max_length=100, min_length=2)
    adress_number = models.CharField(max_length=10, min_length=0)
    
