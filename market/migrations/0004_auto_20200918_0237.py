# Generated by Django 3.1 on 2020-09-17 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20200918_0233'),
    ]

    operations = [
        
        migrations.RemoveField(
            model_name='warehouse',
            name='agents',
        ),
        migrations.AddField(
            model_name='shipper',
            name='employees',
            field=models.ManyToManyField(blank=True, to='market.Employee', verbose_name='کارکنان'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='employees',
            field=models.ManyToManyField(blank=True, to='market.Employee', verbose_name='کارکنان'),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='employees',
            field=models.ManyToManyField(blank=True, to='market.Employee', verbose_name='کارکنان'),
        ),
        migrations.DeleteModel(
            name='Accountant',
        ),
        migrations.DeleteModel(
            name='Cashier',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]