# Generated by Django 2.2.5 on 2020-11-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
