# Django
from django.db import models

# Project
from unidigi.utils.models import BaseModel


class Answer(BaseModel):
    """
    Possible answer to an exam's question.
    It can be true or false (correct) and has a description text of the
    answer itself.
    """

    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    answer = models.CharField(max_length=3000)
    correct = models.BooleanField()

    def __str__(self):
        return self.answer
