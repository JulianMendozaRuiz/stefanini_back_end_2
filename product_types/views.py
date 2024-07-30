from django.shortcuts import render
from rest_framework import generics

from .models import ProductType
from .serializers import ProductTypeSerializer

# Create your views here.


class ProductTypeListCreate(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
