from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'category','images','description')
    
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'seller', 'stock_level')