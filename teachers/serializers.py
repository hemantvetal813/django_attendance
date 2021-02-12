from rest_framework import serializers
from . models import teachers

class teacherSerializer(serializers.ModelSerializer):

    class Meta:
        model=teachers
        fields='__all__'