# Django
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models

# Project
from unidigi.utils.models import BaseModel


class UserManager(UserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Ensure username and email are in lowercase before calling the framework
        implementation of method.
        """
        username = username or ''
        username = username.lower()
        email = email or ''
        email = email.lower()
        return super()._create_user(self, username, email, password, **extra_fields)


class User(BaseModel, AbstractUser):
    """
    User accounts model.
    """

    USERNAME_REGEX = RegexValidator(
        regex='[a0-z9]',
        message='Only letters and numbers allowed.'
    )
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[USERNAME_REGEX],
        error_messages={'unique': 'Username already in use.'}
    )
    email = models.EmailField(
        unique=True,
        error_messages={'unique': 'Email already in use.'}
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username
