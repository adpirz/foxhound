from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have valid email.")

        if not kwargs.get("username"):
            raise ValueError("Users must have valid username")

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(self, email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account
        
class Account(AbstractBaseUser):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=35, unique=True)

    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)

    is_admin = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager();

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email','username','first_name','last_name']

    def __unicode__(self):
        return self.email


    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name




# Create your models here.
