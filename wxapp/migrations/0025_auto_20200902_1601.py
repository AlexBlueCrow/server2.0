# Generated by Django 2.2.5 on 2020-09-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0024_auto_20200902_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captain',
            name='genre',
        ),
        migrations.AlterField(
            model_name='captain',
            name='diliver',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='captain',
            name='marketing',
            field=models.BooleanField(default=False),
        ),
    ]