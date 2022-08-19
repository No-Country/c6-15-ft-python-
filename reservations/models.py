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


class reservations(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    payment_type = models.IntegerField(null=False, blank=False, choices=payments_types , default=1)
    status = models.IntegerField(null=False, blank=False, choices=status_reservations , default=1)
    sitter_publication = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.reservations_id

    class meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservation'
        ordering = ['check_in']
        unique_together = ('check_in', 'check_out', 'sitter_publication')
        constraints = [
            models.UniqueConstraint(fields=['check_in', 'check_out', 'sitter_publication'], name='unique_reservations')
        ]