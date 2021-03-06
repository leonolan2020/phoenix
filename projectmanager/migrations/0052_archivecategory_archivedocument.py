# Generated by Django 3.1 on 2020-10-13 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0051_auto_20201011_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveCategory',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
            ],
            options={
                'verbose_name': 'ArchiveCategory',
                'verbose_name_plural': 'ArchiveCategorys - دسته بندی های اسناد آرشیوی',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='ArchiveDocument',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
            ],
            options={
                'verbose_name': 'ArchiveDocument',
                'verbose_name_plural': 'ArchiveDocuments - اسناد آرشیوی',
            },
            bases=('projectmanager.managerpage',),
        ),
    ]
