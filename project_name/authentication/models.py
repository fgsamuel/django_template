from {{ project_name }}.authentication.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class CustomGroup(Group):
    """Created only to group apps in administrator"""
    class Meta:
        proxy = True
        verbose_name = "Group"
        verbose_name_plural = "Groups"