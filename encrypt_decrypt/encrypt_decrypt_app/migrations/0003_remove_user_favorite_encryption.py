# Generated by Django 3.0.8 on 2020-07-23 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encrypt_decrypt_app', '0002_auto_20200722_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite_encryption',
        ),
    ]
