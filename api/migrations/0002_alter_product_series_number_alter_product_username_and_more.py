# Generated by Django 5.0.7 on 2024-07-30 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='series_number',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='username',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
