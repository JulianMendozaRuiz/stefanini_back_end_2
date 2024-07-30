from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["username", "product_type",
                  "series_number", "delivery_date", "status"]
