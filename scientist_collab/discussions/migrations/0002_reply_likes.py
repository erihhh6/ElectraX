# Generated by Django 5.1.7 on 2025-05-01 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_replies', to=settings.AUTH_USER_MODEL),
        ),
    ]
