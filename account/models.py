from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy  as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('The Username must be set'))
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('user is not staff user.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('user is not superuser.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null=True)
    phone_number = models.IntegerField(null=True)
    password = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
  
    objects = UserManager()
