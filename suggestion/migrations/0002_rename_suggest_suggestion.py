# Generated by Django 4.2.7 on 2023-11-24 10:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suggestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suggest',
            new_name='Suggestion',
        ),
    ]
