# Generated by Django 3.1.6 on 2021-02-16 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('take_attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='take_attendance',
            name='bhs_id',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
