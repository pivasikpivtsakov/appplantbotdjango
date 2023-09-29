from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime


class AccountManager(BaseUserManager):
    def create_superuser(self, email, password, firstname, lastname, **other_fields):
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_admin", True)
        return self.create_user(email, password, firstname, lastname, **other_fields)

    def create_user(self, email, password, firstname, lastname, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname, lastname=lastname,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(verbose_name="login", unique=True, max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    screen_name = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_token = models.CharField(verbose_name="user token", null=True, max_length=100)
    user_token_verified = models.BooleanField(default=False)
    telegram_id = models.IntegerField(null=True)

    objects = AccountManager()

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ("screen_name", )

    def __str__(self):
        return self.screen_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
