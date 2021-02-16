# Django
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

# Project
from unidigi.users.models import User
from unidigi.users.forms import SignupForm


def signup(request):    

    if request.method == 'POST':
        return perform_signup(request)
    elif request.method == 'GET':
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
        messages.add_message(request, messages.SUCCESS, _('Your account has been registered!'))
        return redirect('login')
    return redirect('signup')
