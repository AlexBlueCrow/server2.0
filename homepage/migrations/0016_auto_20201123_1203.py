# Generated by Django 2.2.5 on 2020-11-23 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_bankinfo_banknum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='role',
            field=models.CharField(choices=[('farmuser', 'farmuser'), ('manager', 'manager'), ('admin', 'admin')], default='farmuser', max_length=20),
        ),
    ]
