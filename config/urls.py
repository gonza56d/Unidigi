"""
unidigi URL Configuration
https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

# Django
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('unidigi.users.urls')),
]
