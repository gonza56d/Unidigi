# Django
from django.shortcuts import redirect, render

# Project
from unidigi.users.models import User
from unidigi.users.forms import SignupForm


def signup(request):

    form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


def perform_signup(request):

    form = SignupForm(data=request.POST)
    if form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data.get('username'),
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password'),
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name')
        )
        return redirect('login')
    else:
        form = SignupForm()
        errors = form.errors
        return render(request, 'users/signup.html', {'form': form, 'errors': errors})

