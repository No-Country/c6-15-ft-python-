from django.db import models
from homepage.models import User

# Create your models here.
class Sitter(models.Model):
    price = models.IntegerField()
    descripcion = models.charField()
    status = models.BooleanField(default=True)
    picture_site = models.ImageField(upload_to='sitter/img/') 
    #user relationship
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.Sitter

    class meta:
        verbose_name = 'Sitter'
        verbose_name_plural = 'Sitters'