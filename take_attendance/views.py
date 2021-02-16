from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import take_attendance
from . serializers import take_attendance_serializer
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['POST'])
def add(request):
    serializer = take_attendance_serializer(take_attendance(),request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data,status=200)
    return Response(serializer.errors,status=400)