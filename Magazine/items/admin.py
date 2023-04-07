from django.contrib import admin

from .models import  *


@admin.register(Product,Characteristic)
class Register_all(admin.ModelAdmin):
    pass