# Generated by Django 2.2.5 on 2020-08-26 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0009_remove_adopt_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price_origin',
        ),
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wxapp.Item'),
        ),
    ]
