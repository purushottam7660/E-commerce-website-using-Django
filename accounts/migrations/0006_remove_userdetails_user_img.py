# Generated by Django 5.0.3 on 2024-04-27 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_userdetails_user_userdetails_user_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='user_img',
        ),
    ]
