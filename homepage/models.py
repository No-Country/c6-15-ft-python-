from enum import unique
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=10)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    adress_street = models.CharField(max_length=100)
    adress_number = models.CharField(max_length=10)
    user_type = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name.username

    class meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

