from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator
# from django.contrib.auth import forms

# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, **other):
        user = self.model(email=username, username=username, **other)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, email=None, username=None, password=None, **other):
        other.setdefault('is_superuser', False)
        other.setdefault('is_staff', False)
        return self._create_user(username, password, **other)

    def create_superuser(self, email=None, username=None, password=None, **other):
        other.setdefault('is_superuser', True)
        other.setdefault('is_staff', True)

        return self._create_user(username, password, **other)


class User(AbstractUser):
    username = models.CharField(max_length=16, blank=True, default='', unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    joined = models.DateTimeField(
        editable=False, null=True, auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username