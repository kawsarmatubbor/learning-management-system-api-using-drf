from django.db import models
from django.contrib.auth.models import AbstractUser
from . import manager

# User model customization
class CustomUser(AbstractUser):
    USER_ROLE = (
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    )
    username = None
    phone_number = models.CharField(max_length=14, unique=True)
    role = models.CharField(max_length=50, choices=USER_ROLE, default='student')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = manager.CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"