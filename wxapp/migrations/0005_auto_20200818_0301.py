# Generated by Django 2.2.5 on 2020-08-18 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0004_auto_20200814_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captain',
            name='commission_d',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='captain',
            name='commission_m',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='captain',
            name='phonenumber',
            field=models.BigIntegerField(default=0),
        ),
    ]
