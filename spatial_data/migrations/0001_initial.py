# Generated by Django 4.2.7 on 2025-07-24 08:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpatialPolygon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('polygon', models.TextField()),
                ('category', models.CharField(choices=[('city', 'City'), ('district', 'District'), ('park', 'Park'), ('water', 'Water Body'), ('forest', 'Forest'), ('agricultural', 'Agricultural Land'), ('industrial', 'Industrial Zone'), ('residential', 'Residential Area'), ('other', 'Other')], default='other', max_length=50)),
                ('area_sq_meters', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['category'], name='spatial_dat_categor_27741c_idx'), models.Index(fields=['created_at'], name='spatial_dat_created_0fbb1b_idx')],
            },
        ),
        migrations.CreateModel(
            name='SpatialPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('point', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('park', 'Park'), ('restaurant', 'Restaurant'), ('hospital', 'Hospital'), ('school', 'School'), ('shopping', 'Shopping Center'), ('transport', 'Transport Hub'), ('other', 'Other')], default='other', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['category'], name='spatial_dat_categor_8da98d_idx'), models.Index(fields=['created_at'], name='spatial_dat_created_195d39_idx')],
            },
        ),
    ]
