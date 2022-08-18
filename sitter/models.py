from django.db import models
from django.contrib.auth.models import User

status_pub = [
    (1, 'Activa'),
    (2, 'Inactiva'),
]


# Create your models here.
class Sitter(models.Model):
    price = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    status = models.IntegerField(null=False, blank=False, choices=status_pub , default=1)
    picture_site = models.ImageField(upload_to='sitter/static/img/', blank=True)
    #user relationship
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_id.username

    class meta:
        verbose_name = 'Sitter'
        verbose_name_plural = 'Sitters'
