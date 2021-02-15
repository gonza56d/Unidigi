"""User urls."""

# Django
from django.urls import path

# Project
from unidigi.users.views import signup


urlpatterns = [
    path('signup/', signup, name='signup'),
]
