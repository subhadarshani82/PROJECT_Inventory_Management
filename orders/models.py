from django.db import models
from accounts.models import CustomUser
from products.models import*
# Create your models here.
class Order(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'seller'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending')

    def __str__(self):
        return f"Order {self.id} - {self.product.name}"