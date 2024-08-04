from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


# Create your models here.

class User(AbstractUser):
    number = models.CharField(unique=True, max_length=11)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'number'

    objects = CustomUserManager()
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.number
