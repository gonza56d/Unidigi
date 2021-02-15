# Django
from django import forms

# Project
from unidigi.users.models import User


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()
