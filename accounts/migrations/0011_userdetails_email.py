# Generated by Django 5.0.3 on 2024-04-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_userdetails_user_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]