from django.db import models
from homepage.models import User

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    size = models.IntegerField()
    condition = models.CharField(max_length=255)
    accesories = models.CharField(max_length=255)
    #user relationships
    petowner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.Pet
    
    class meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    