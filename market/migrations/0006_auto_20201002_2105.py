# Generated by Django 3.1 on 2020-10-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20201002_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='origin_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت بدون تخفیف'),
        ),
    ]
