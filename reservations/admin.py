from django.contrib import admin
from .models import Reservations
# Register your models here.

class reservationsAdmin(admin.ModelAdmin):
    list_display = ('check_in', 'check_out', 'sitter_publication', 'user_id', 'payment_type', 'status')

admin.site.register(Reservations)