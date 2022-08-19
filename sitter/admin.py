from django.contrib import admin
from .models import Sitter
# Register your models here.


class SitterAdmin(admin.ModelAdmin):
    list_display = ( 'user_id','price', 'descripcion','status', 'picture_site')
    ordering = ('user_id',)
    search_fields = ('user_id__username','price','descripcion','status')



admin.site.register(Sitter, SitterAdmin)

