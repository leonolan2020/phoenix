# Generated by Django 3.1 on 2020-09-29 21:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200930_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='jumbotron',
            name='full_description',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True, verbose_name='شرح کامل html'),
        ),
    ]