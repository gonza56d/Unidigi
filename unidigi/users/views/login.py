# Django
from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

# Project
from unidigi.users.forms import LoginForm


def login(request):
    """
    Redirect to login panel page.
    """
    if request.method == 'POST':
        return perform_login(request)
    elif request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


def perform_login(request):
    """
    Receive authentication credentials and try to login.
    """
    form = LoginForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, _('Log in succes.'))
            return redirect('index')
        else:
            messages.add_message(request, messages.WARNING, _('Wrong username/password.'))
    return redirect('login')


def perform_logout(request):
    """
    Handle logout request logging out the current user session.
    """
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, _('You have logged out.'))
    return redirect('index')
