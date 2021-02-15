"""Users admin module."""

# Django
from django.contrib import admin

# Project
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'created', 'modified')
    search_fields = ('username', 'email', 'created', 'modified')
    list_filter = ('username', 'email', 'created', 'modified')
