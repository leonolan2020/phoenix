# Generated by Django 3.1 on 2020-11-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_auto_20201011_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='list_for_app',
            field=models.BooleanField(default=False, verbose_name='نمایش در صفحه اصلی سایت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='for_home',
            field=models.BooleanField(default=False, verbose_name='نمایش در صفحه فروشگاه'),
        ),
    ]
