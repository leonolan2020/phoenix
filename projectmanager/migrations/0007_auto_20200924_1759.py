# Generated by Django 3.1 on 2020-09-24 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0010_auto_20200923_0246'),
        ('projectmanager', '0006_auto_20200924_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='projectmanager/images/Page/Images/', verbose_name='Image')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='projectmanager/images/Page/thumbnails/', verbose_name='thumbnail')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='ManagerPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pretitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('posttitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='شرح کوتاه')),
                ('description', models.TextField(blank=True, null=True, verbose_name='شرح کامل')),
                ('action_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='متن دکمه')),
                ('action_url', models.CharField(blank=True, max_length=2000, null=True, verbose_name='لینک دکمه')),
                ('video_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='متن ویدیو')),
                ('video_url', models.CharField(blank=True, max_length=2000, null=True, verbose_name='لینک ویدیو')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('image_header_origin', models.ImageField(blank=True, null=True, upload_to='projectmanager/images/Page/', verbose_name='تصویر سربرگ')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date_updated')),
                ('images', models.ManyToManyField(blank=True, to='projectmanager.Image', verbose_name='تصویر ها')),
                ('meta_datas', models.ManyToManyField(blank=True, to='app.MetaData', verbose_name='meta_datas')),
                ('tags', models.ManyToManyField(blank=True, to='app.Tag', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='MaterialObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(blank=True, max_length=200, null=True, verbose_name='serial_no')),
                ('barcode1', models.CharField(blank=True, max_length=200, null=True, verbose_name='barcode1')),
                ('borcode2', models.CharField(blank=True, max_length=200, null=True, verbose_name='barcode2')),
                ('barcode3', models.CharField(blank=True, max_length=200, null=True, verbose_name='barcode3')),
                ('package_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='package_no')),
                ('package_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='package_name')),
            ],
            options={
                'verbose_name': 'MaterialObject',
                'verbose_name_plural': 'MaterialObjects',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('model', models.CharField(max_length=50, verbose_name='model')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='MaterialBrand',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس اینترتی')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='MaterialWareHouse',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('location', models.CharField(blank=True, max_length=50, null=True, verbose_name='location')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='address')),
            ],
            options={
                'verbose_name': 'MaterialWareHouse',
                'verbose_name_plural': 'MaterialWareHouses',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
            ],
            options={
                'verbose_name': 'ProjectCategory',
                'verbose_name_plural': 'ProjectCategories',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='PageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('action', models.CharField(max_length=50, verbose_name='action')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projectmanager.managerpage', verbose_name='page')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='ایجاد کننده')),
            ],
            options={
                'verbose_name': 'PageLog',
                'verbose_name_plural': 'PageLogs',
            },
        ),
        migrations.CreateModel(
            name='MaterialPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_no', models.CharField(max_length=50, verbose_name='pack_no')),
                ('material_objects', models.ManyToManyField(to='projectmanager.MaterialObject', verbose_name='material_objects')),
            ],
            options={
                'verbose_name': 'MaterialPackage',
                'verbose_name_plural': 'MaterialPackages',
            },
        ),
        migrations.CreateModel(
            name='MaterialLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=50, verbose_name='priority')),
                ('log_type', models.CharField(max_length=50, verbose_name='log_type')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('material_object', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='material_object', to='projectmanager.materialobject')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to='app.profile')),
            ],
            options={
                'verbose_name': 'MaterialPackage',
                'verbose_name_plural': 'MaterialPackages',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('نگهبان', 'نگهبان'), ('مدیر', 'مدیر'), ('فنی', 'فنی'), ('تایید نشده', 'تایید نشده'), ('حسابدار', 'حسابدار'), ('صندوقدار', 'صندوقدار')], default='تایید نشده', max_length=50, verbose_name='نقش')),
                ('degree', models.CharField(choices=[('دیپلم', 'دیپلم'), ('کاردانی', 'کاردانی'), ('کارشناسی', 'کارشناسی'), ('کارشناسی ارشد', 'کارشناسی ارشد'), ('دکتری', 'دکتری')], default='کارشناسی', max_length=50, verbose_name='مدرک')),
                ('major', models.CharField(blank=True, max_length=50, null=True, verbose_name='رشته تحصیلی')),
                ('introducer', models.CharField(blank=True, max_length=50, null=True, verbose_name='معرف')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='emp', to='app.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='WorkUnit',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('employees', models.ManyToManyField(blank=True, to='projectmanager.Employee', verbose_name='نیروی انسانی')),
            ],
            options={
                'verbose_name': 'WorkUnit',
                'verbose_name_plural': 'WorkUnits',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('location', models.CharField(blank=True, max_length=500, null=True, verbose_name='موقعیت در نقشه گوگل 400*400')),
                ('status', models.CharField(choices=[('پیش فرض', 'پیش فرض'), ('در حال انجام', 'در حال انجام'), ('آماده سازی اولیه', 'آماده سازی اولیه'), ('انجام شده', 'انجام شده'), ('تحویل شده', 'تحویل شده'), ('درحال آنالیز', 'درحال آنالیز')], default='پیش فرض', max_length=50, verbose_name='status')),
                ('amount', models.IntegerField(default=0, verbose_name='مبلغ')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectmanager.projectcategory', verbose_name='category')),
                ('material_warehouses', models.ManyToManyField(blank=True, to='projectmanager.MaterialWareHouse', verbose_name='material_warehouses')),
                ('work_units', models.ManyToManyField(blank=True, to='projectmanager.WorkUnit', verbose_name='work_units')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.AddField(
            model_name='materialwarehouse',
            name='employees',
            field=models.ManyToManyField(blank=True, to='projectmanager.Employee', verbose_name='employees'),
        ),
        migrations.AddField(
            model_name='materialobject',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanager.material', verbose_name='material'),
        ),
        migrations.CreateModel(
            name='MaterialCategory',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projectmanager.materialcategory', verbose_name='دسته بندی بالاتر')),
            ],
            options={
                'verbose_name': 'MaterialCategory',
                'verbose_name_plural': 'MaterialCategories',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.AddField(
            model_name='material',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanager.materialbrand', verbose_name='brand'),
        ),
        migrations.AddField(
            model_name='material',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='material_category', to='projectmanager.materialcategory'),
        ),
    ]
