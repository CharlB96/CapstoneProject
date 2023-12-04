# Generated by Django 4.2.7 on 2023-12-04 11:23

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedia', '0008_remove_article_iframe_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='map',
            field=cloudinary.models.CloudinaryField(default='placeholder-map', max_length=255, verbose_name='map'),
        ),
        migrations.AddField(
            model_name='article',
            name='map_alt',
            field=models.CharField(default='map', max_length=50),
        ),
    ]