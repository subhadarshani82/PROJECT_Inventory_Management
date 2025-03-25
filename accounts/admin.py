from django.contrib import admin
from accounts.models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display=['id','role','username']
    
    
admin.site.register(CustomUser,CustomUserAdmin)