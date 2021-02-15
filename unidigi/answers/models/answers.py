# Django
from django.db import models

# Project
from unidigi.utils.models import BaseModel


class Answer(BaseModel):

    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    answer = models.CharField(max_length=3000)
    correct = models.BooleanField()

    def __str__(self):
        return self.answer
