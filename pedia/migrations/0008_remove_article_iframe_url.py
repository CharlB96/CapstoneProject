# Generated by Django 4.2.7 on 2023-12-04 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedia', '0007_article_iframe_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='iframe_url',
        ),
    ]