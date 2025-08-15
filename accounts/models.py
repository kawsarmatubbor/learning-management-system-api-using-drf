from django.db import models
from django.contrib.auth.models import AbstractUser
from . import manager

# User model customization
class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=14, unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = manager.CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"