# Generated by Django 2.2.5 on 2020-08-26 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0007_remove_item_price2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='item',
            name='unit',
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('unit', models.CharField(default='', max_length=15)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Sell', to='wxapp.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Adopt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('guaranteed', models.FloatField(default=0)),
                ('benefit', models.CharField(max_length=200)),
                ('period', models.IntegerField(blank=True, default=1)),
                ('unit', models.CharField(default='', max_length=5)),
                ('sign', models.CharField(max_length=20)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Adopt', to='wxapp.Item')),
            ],
        ),
    ]
