# Generated by Django 3.1 on 2020-10-04 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0037_auto_20201004_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='title',
            field=models.CharField(default='-', max_length=100, verbose_name='عنوان'),
            preserve_default=False,
        ),
    ]
