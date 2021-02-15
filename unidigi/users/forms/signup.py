# Django
from django import forms

# Project
from unidigi.profiles.models import Profile
from unidigi.users.models import User


class SignupForm(forms.ModelForm):

    re_password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    kind = forms.ChoiceField(choices=Profile.Kinds.choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput() 
        self.fields['re_password'].widget = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
