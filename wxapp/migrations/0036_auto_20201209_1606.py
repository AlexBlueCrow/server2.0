# Generated by Django 2.2.5 on 2020-12-09 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0035_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='correct_anwser',
            new_name='correct_answer',
        ),
    ]