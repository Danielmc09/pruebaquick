from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.
from .managers import UserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user( email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
            return self._create_user( email, password, True, True, **extra_fields)


class Clients(AbstractBaseUser, PermissionsMixin):
    documento = models.CharField(max_length = 20, unique = True, blank=True, null=True)
    email = models.EmailField('Email',max_length = 255, unique = True)
    first_name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email