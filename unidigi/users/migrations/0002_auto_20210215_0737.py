# Generated by Django 3.1.6 on 2021-02-15 07:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'Username already in use.'}, max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Only lowercase letters and numbers allowed.', regex='[a0-z9]')]),
        ),
    ]
