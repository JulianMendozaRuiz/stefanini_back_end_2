from django.db import models

# Create your models here.


class Product (models.Model):
    username = models.CharField(max_length=400)
    product_type = models.CharField(max_length=400)
    series_number = models.CharField(max_length=400)
    delivery_date = models.DateField()
    status = models.CharField(max_length=400)

    def __str__(self):
        return self.series_number
