from django.db import models

# Create your models here.


class ProductType(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name
