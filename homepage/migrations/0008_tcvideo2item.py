# Generated by Django 2.2.5 on 2020-11-15 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0033_auto_20201021_0850'),
        ('homepage', '0007_tcvideo_time_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='tcVideo2Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wxapp.Item')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.TcVideo')),
            ],
        ),
    ]
