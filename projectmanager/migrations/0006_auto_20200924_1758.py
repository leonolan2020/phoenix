# Generated by Django 3.1 on 2020-09-24 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0005_auto_20200924_1753'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectCategory',
        ),
    ]
