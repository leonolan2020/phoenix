# Generated by Django 3.1 on 2020-09-22 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0008_financialdocument_child_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialdocument',
            name='child_class',
            field=models.CharField(blank=True, max_length=50, verbose_name='child_class'),
        ),
    ]