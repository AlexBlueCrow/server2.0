# Generated by Django 2.2.5 on 2020-08-31 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0021_auto_20200831_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='captain_obj',
            new_name='cap',
        ),
    ]
