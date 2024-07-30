from rest_framework import serializers
from .models import ProductType, Product

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "username", "product_type", "series_number", "delivery_date"]