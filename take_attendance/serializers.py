from rest_framework import serializers
from . models import take_attendance

class take_attendance_serializer(serializers.ModelSerializer):

    class Meta:
        model=take_attendance
        fields='__all__'