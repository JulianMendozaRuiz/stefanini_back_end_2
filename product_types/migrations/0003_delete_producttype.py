# Generated by Django 4.1.13 on 2024-07-30 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_types', '0002_producttype_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductType',
        ),
    ]
