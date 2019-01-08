from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework import generics
from portfolio import models
from . import serializers 

class ListProjects(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProyectoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
