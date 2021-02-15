# Django
from django import forms

# Project
from unidigi.profiles.models import Profile


class SignupForm(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    re_password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    kind = forms.ChoiceField(choices=Profile.Kinds.choices)
