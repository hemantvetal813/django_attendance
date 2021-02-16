from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class take_attendance(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField()
    bhs_id=models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    is_present=models.CharField(max_length=1, validators=[MinLengthValidator(1)])
    insert_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name