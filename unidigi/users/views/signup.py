# Django
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

# Project
from ..forms import SignupForm
from unidigi.users import services


def signup(request):    
    """
    Redirect to signup business logic if post.
    Redirect to account registration page if get.
    """
    if request.method == 'POST':
        return perform_signup(request)
    elif request.method == 'GET':
        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form})


def perform_signup(request):
    """
    Receive new account request and try to sign up.
    """
    form = SignupForm(data=request.POST)
    if form.is_valid():
        services.perform_signup(
            username=form.cleaned_data.get('username'),
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password'),
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            profile_type=form.cleaned_data.get('profile_type')
        )
        messages.add_message(request, messages.SUCCESS, _('Your account has been registered!'))
        return redirect('login')
    for errors in form.errors.values():
        [messages.add_message(request, messages.WARNING, error) for error in errors]
    return redirect('signup')
