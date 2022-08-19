from django.contrib import admin
from .models import Pet

# Register your models here.


class PetAdmin(admin.ModelAdmin):
    list_display = ( 'user_id','name', 'age','size', 'condition')
    ordering = ('user_id',)
    search_fields = ('user_id__username','name','age','size','condition')


admin.site.register(Pet, PetAdmin)


