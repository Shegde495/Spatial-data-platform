# Generated by Django 4.2.7 on 2025-07-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spatial_data', '0005_spatialpolygon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spatialpoint',
            name='category',
            field=models.CharField(default='other', max_length=50),
        ),
        migrations.AlterField(
            model_name='spatialpolygon',
            name='category',
            field=models.CharField(default='other', max_length=50),
        ),
    ]
