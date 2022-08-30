from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from sitter.models import Sitter
# Create your models here.

payments_types = [
    (1, 'Efectivo'),
    (2, 'Tarjeta de crédito'),
    (3, 'Tarjeta de débito'),
    (4, 'Paypal'),

]

status_reservations = [
    (1, 'cancelar'),
    (2, 'confirmar'),
]


class Reservations(models.Model):
    sitter_publication = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    payment_type = models.IntegerField(null=False, blank=False, choices=payments_types , default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.IntegerField(null=False, blank=False, choices=status_reservations , default=2)


    def __str__(self):
        return f'{self.reservation_date}'

    class meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservation'
         