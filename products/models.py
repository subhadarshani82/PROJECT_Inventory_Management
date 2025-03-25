from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('home_appliances', 'Home Appliances'),
        ('books', 'Books'),
        ('beauty', 'Beauty & Personal Care'),
        ('sports', 'Sports & Fitness'),
        ('toys', 'Toys & Games'),
    )
    name=models.CharField(max_length=255)
    description = models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    images = models.ImageField(upload_to='product_images/',blank=True,null=True)
    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    seller=models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'role':'Seller'})
    stock_level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.stock_level}"