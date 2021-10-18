from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, document, email, password, is_staff, is_superuser, **extra_fields ):
        user = self.model(
            document=document,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, document, email, password=None, **extra_fields):
        return self._create_user(document, email, password, False, False,  **extra_fields)

    def create_superuser(self, document, email, password=None, **extra_fields):
        return self._create_user(document, email, password, True, True, **extra_fields)
