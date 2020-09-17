# Generated by Django 3.1 on 2020-09-17 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200918_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('jumbotron_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.jumbotron')),
                ('image_origin', models.ImageField(upload_to='app/images/Gallery/Photo/', verbose_name='Big Image 345*970 ')),
                ('for_home', models.BooleanField(default=False, verbose_name='Show on homepage')),
                ('archive', models.BooleanField(default=False, verbose_name='Archive?')),
                ('priority', models.IntegerField(default=100, verbose_name='Priority')),
                ('thumbnail_origin', models.ImageField(blank=True, null=True, upload_to='app/images/Gallery/Photo/Thumbnail/', verbose_name='Thumbnail Image')),
            ],
            options={
                'verbose_name': 'GalleryPhoto',
                'verbose_name_plural': 'تصاویر',
            },
            bases=('app.jumbotron',),
        ),
        migrations.CreateModel(
            name='GalleryAlbum',
            fields=[
                ('jumbotron_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.jumbotron')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='app/images/Gallery/Album/', verbose_name='Big Image 345*970 ')),
                ('for_home', models.BooleanField(default=False, verbose_name='Show on homepage')),
                ('archive', models.BooleanField(default=False, verbose_name='Archive?')),
                ('priority', models.IntegerField(default=100, verbose_name='Priority')),
                ('thumbnail_origin', models.ImageField(blank=True, null=True, upload_to='app/images/Gallery/Album/Thumbnail/', verbose_name='Thumbnail Image')),
                ('photos', models.ManyToManyField(blank=True, to='app.GalleryPhoto', verbose_name='Photos')),
            ],
            options={
                'verbose_name': 'GalleryAlbum',
                'verbose_name_plural': 'آلبوم های تصاویر',
            },
            bases=('app.jumbotron',),
        ),
    ]
