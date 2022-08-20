from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    street        = models.CharField(max_length=20)
    zip           = models.IntegerField()
    city          = models.CharField(max_length=100)
    country       = models.CharField(max_length=100)
    photo         = models.ImageField('User profile',upload_to="users/",
                                      null=True, blank=True)
    stars_average = models.IntegerField()
    user          = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)
    