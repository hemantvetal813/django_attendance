from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class teachers(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, validators=[MinLengthValidator(4)])
    email=models.CharField(max_length=50, validators=[MinLengthValidator(4)])
    password=models.CharField(max_length=50, validators=[MinLengthValidator(8)])
    insert_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name