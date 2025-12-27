from django.db import models
from django.contrib.auth.models import AbstractUser

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created_at' and 'updated_at' fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    """
    Custom User model to easily add fields later (e.g., is_verified, phone_number)
    """
    email = models.EmailField(unique=True)
    
    # We want email to be the unique identifier, not username? 
    # (Optional: configure USERNAME_FIELD = 'email' if you want)