# Django
from django.shortcuts import render

# Project
from unidigi.users.forms import LoginForm


def login(request):

    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
