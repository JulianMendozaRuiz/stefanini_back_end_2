from django.shortcuts import render
from rest_framework import generics

from .models import ProductType, Product
from .seriealizers import ProductTypeSerializer, ProductSerializer

# Create your views here.


class ProductTypeListCreate(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
