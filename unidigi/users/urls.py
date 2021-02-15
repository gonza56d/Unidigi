"""User urls."""

# Django
from django.urls import path

# Project
from unidigi.users.views import login, signup


urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]
