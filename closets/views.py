from django.shortcuts import render

# Create your views here.
from .models import Closet
from .serializers import ClosetSerializer
from rest_framework import generics

class ClosetListCreate(generics.ListCreateAPIView):
    queryset = Closet.objects.all()
    serializer_class = ClosetSerializer