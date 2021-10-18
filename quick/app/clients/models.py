from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
from .managers import UserManager

class Clients(AbstractBaseUser, PermissionsMixin):
    document = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    #Si quiere que ingrese al admin el is_staff debe estar en true
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'document'

    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    def __str__(self):
        return self.document
