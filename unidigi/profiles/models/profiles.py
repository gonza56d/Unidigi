# Django
from django.db import models

# Project
from unidigi.utils.models import BaseModel, CommonRegex


class Profile(BaseModel):
    """
    Representation of users' profile.
    """

    class ProfileTypes(models.TextChoices):
        """
        profile_type constants.
        Users can have profile of either teachers or students.
        """
        TEACHER = 'T', 'Teacher'
        STUDENT = 'S', 'Student'

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    profile_type = models.CharField(max_length=1, choices=ProfileTypes.choices)
    first_name = models.CharField(max_length=100, validators=[CommonRegex.LETTERS])
    last_name = models.CharField(max_length=100, validators=[CommonRegex.LETTERS])
    birthday = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='profiles', blank=True)
    bio = models.CharField(max_length=3000, null=True, blank=True)
