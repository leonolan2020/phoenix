# Generated by Django 3.1 on 2020-09-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200923_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='signature',
            name='status',
            field=models.CharField(default='sdsd', max_length=200, verbose_name='status'),
            preserve_default=False,
        ),
    ]
