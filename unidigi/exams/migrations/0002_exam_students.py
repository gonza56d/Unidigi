# Generated by Django 3.1.6 on 2021-02-15 22:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studentexams', '0001_initial'),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='students',
            field=models.ManyToManyField(related_name='student_exams', through='studentexams.StudentExam', to=settings.AUTH_USER_MODEL),
        ),
    ]
