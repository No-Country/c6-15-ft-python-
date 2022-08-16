from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sitter(models.Model):
    price = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    picture_site = models.ImageField(upload_to='sitter/img/') 
    #user relationship
    sitter_id = models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.sitter_id.username

    
    class meta:
        verbose_name = 'Sitter'
        verbose_name_plural = 'Sitters'