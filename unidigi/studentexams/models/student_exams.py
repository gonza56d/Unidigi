# Django
from django.db import models

from unidigi.utils.models import BaseModel


class StudentExam(BaseModel):
    """
    ManyToMany relationship that indicates what exams are the students allowed
    to take.
    It stores the date time when the student starts the exam and also the
    finish date time.
    """
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    exam = models.ForeignKey('exams.Exam', on_delete=models.CASCADE)
    started = models.DateTimeField(null=True, blank=True)
    finished = models.DateTimeField(null=True, blank=True)
