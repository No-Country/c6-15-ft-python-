from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    size = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    accesories = models.CharField(max_length=255)
    #user relationships

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    class meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    