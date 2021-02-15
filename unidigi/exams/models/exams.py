# Django
from django.db import models

# Project
from unidigi.utils.models import BaseModel


class Exam(BaseModel):
    """
    Exam created by a teacher user.
    Minutes attribute represents how many minutes students have to finish the
    exam. It can be null to allow students to have infinite time to finish.
    Deadline attribute represents the date until the exam is available. After
    this date, students won't be able to take the exam. It can be null so that
    students can take the exam with no delivery date.
    """
    
    teacher = models.ForeignKey('users.User', on_delete=models.CASCADE)
    students = models.ManyToManyField(
        'users.User',
        through='studentexams.StudentExam',
        related_name='student_exams'
    )
    exam = models.CharField(max_length=50)
    minutes = models.PositiveIntegerField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.exam
