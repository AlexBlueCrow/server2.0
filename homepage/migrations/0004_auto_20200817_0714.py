# Generated by Django 2.2.5 on 2020-08-17 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200814_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videofiles',
            name='description',
        ),
        migrations.RemoveField(
            model_name='videofiles',
            name='itemname',
        ),
    ]
