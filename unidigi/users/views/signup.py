# Django
from django.shortcuts import render

# Project
from unidigi.users.forms import SignupForm


def signup(request):

    form = SignupForm()
    return render(request, 'signup.html', {'form': form})
