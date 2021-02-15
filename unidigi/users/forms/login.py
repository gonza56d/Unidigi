# Django
from django import forms

# Project
from unidigi.users.models import User


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
