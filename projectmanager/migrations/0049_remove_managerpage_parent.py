# Generated by Django 3.1 on 2020-10-08 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0048_auto_20201008_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managerpage',
            name='parent',
        ),
    ]
