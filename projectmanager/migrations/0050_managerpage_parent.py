# Generated by Django 3.1 on 2020-10-08 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0049_remove_managerpage_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='managerpage',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_page', to='projectmanager.managerpage', verbose_name='parent'),
        ),
    ]
