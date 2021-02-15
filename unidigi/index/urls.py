"""Index urls."""

# Django
from django.urls import path

# Project
from unidigi.index.views import index


urlpatterns = [
    path('', index, name='index'),
]
