"""Users business logic module."""

# Django
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

# Project
from .models import User


def perform_signup(username, email, password, first_name, last_name, profile_type):
    """
    User signup business logic.
    """
    User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        profile_type=profile_type
    )
