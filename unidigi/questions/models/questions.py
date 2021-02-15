# Django
from django.db import models

# Project
from unidigi.utils.models import BaseModel


class Question(BaseModel):

    exam = models.ForeignKey('exams.Exam', on_delete=models.CASCADE)
    question = models.CharField(max_length=5000)

    def __str__(self):
        return self.question
