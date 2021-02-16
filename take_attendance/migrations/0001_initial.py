# Generated by Django 3.1.6 on 2021-02-16 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='take_attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('bhs_id', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4)])),
                ('is_present', models.CharField(max_length=1, validators=[django.core.validators.MinLengthValidator(1)])),
                ('insert_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
