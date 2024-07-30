from django.db import models

# Create your models here.


class ProductType(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Product (models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40)
    product_type = models.ForeignKey(
        ProductType, on_delete=models.SET_NULL, blank=True, null=True)
    series_number = models.CharField(max_length=40)
    delivery_date = models.DateField()

    def __str__(self):
        return self.series_number
