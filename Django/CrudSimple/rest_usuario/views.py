from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Blog.models import Blog
from .serializers import BlogSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET','POST'])
def lista_Blog(request):
    """
    LISTA TODOS LOS USUARIOS
    """
    if request.method == 'GET':
        usuario = Blog.objects.all()
        serializer = BlogSerializer(usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_Blog(request, id):
    """
    Métodos disponibles para gestionar datos
    """
    try:
        usuario = Blog.objects.get(BlogId=id)
    except Usuario.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BlogSerializer(usuario)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
