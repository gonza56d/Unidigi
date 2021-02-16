"""User urls."""

# Django
from django.urls import path

# Project
from unidigi.users.views import login, perform_logout, signup


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', perform_logout, name='logout'),
    path('signup/', signup, name='signup'),
]
