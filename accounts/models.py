from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    role_choices=(
        ("Distributor","Distributor"),
        ("Seller","Seller"),
        ("Admin","Admin"),)
    role=models.CharField(max_length=20,choices=role_choices)
    
    
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        blank=True,
        help_text="Specific permissions for this user.",
    )
    def __str__(self):
        return self.username