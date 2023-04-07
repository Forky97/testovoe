from django.db import models
from django.contrib.auth.models import User



class Characteristic(models.Model):
    characteristic_key = models.CharField(max_length=255)
    characteristic_value = models.CharField(max_length=255)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='characteristics')

    def __str__(self):
        return f'{self.characteristic_key}: {self.characteristic_value}'
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


