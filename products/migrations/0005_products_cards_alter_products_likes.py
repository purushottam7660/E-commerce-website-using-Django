# Generated by Django 5.0.3 on 2024-04-12 18:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='cards',
            field=models.ManyToManyField(blank=True, related_name='card_products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='products',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
