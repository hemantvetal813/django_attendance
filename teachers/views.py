from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import teachers
from . serializers import teacherSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET'])
def get(request):
    res= teachers.objects.all()
    serializer=teacherSerializer(res,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getId(request,pk):
    res= teachers.objects.get(id=pk)
    serializer=teacherSerializer(res,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        email = request.data['email']
        password = request.data['password']
        res= teachers.objects.get(email=email,password=password)
        serializer=teacherSerializer(res,many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response('User Not Found')


@api_view(['POST'])
def post(request):
    serializer = teacherSerializer(teachers(),request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data,status=200)
    return Response(serializer.errors,status=400)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update(request):
    id = request.data['id']
    res= teachers.objects.get(id=id)
    serializer=teacherSerializer(res,data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=400)