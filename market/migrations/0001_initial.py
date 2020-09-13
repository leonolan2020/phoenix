# Generated by Django 3.1 on 2020-09-13 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0004_remove_homeslider_for_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='پیش تعریف')),
                ('name', models.CharField(max_length=50, verbose_name='نام برند')),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='توضیحات')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='market/images/Brand/', verbose_name='تصویر')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('priority', models.IntegerField(default=1000, verbose_name='ترتیب')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس اینترتی')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'برند ها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(choices=[('account_circle', 'account_circle'), ('add_shopping_cart', 'add_shopping_cart'), ('alarm', 'alarm'), ('attach_file', 'attach_file'), ('attach_money', 'attach_money'), ('backup', 'backup'), ('build', 'build'), ('chat', 'chat'), ('dashboard', 'dashboard'), ('delete', 'delete'), ('description', 'description'), ('face', 'face'), ('favorite', 'favorite'), ('get_app', 'get_app'), ('help_outline', 'help_outline'), ('home', 'home'), ('important_devices', 'important_devices'), ('link', 'link'), ('local_shipping', 'local_shipping'), ('lock', 'lock'), ('mail', 'mail'), ('notification_important', 'notification_important'), ('psychology', 'psychology'), ('publish', 'publish'), ('reply', 'reply'), ('schedule', 'schedule'), ('send', 'send'), ('settings', 'settings'), ('share', 'share'), ('sync', 'sync'), ('vpn_key', 'vpn_key')], default='important_devices', max_length=50, verbose_name='icon')),
                ('prefix', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='پیش تعریف')),
                ('name', models.CharField(max_length=50, verbose_name='نام دسته')),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='توضیحات')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='market/images/Category/', verbose_name='تصویر')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('priority', models.IntegerField(default=1000, verbose_name='ترتیب')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='market.category', verbose_name='دسته بندی بالاتر')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'مشتریان',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('دیپلم', 'دیپلم'), ('کاردانی', 'کاردانی'), ('کارشناسی', 'کارشناسی'), ('کارشناسی ارشد', 'کارشناسی ارشد'), ('دکتری', 'دکتری')], default='کارشناسی', max_length=50, verbose_name='degree')),
                ('major', models.CharField(max_length=50, verbose_name='major')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'کارمندان',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('درحال پردازش', 'درحال پردازش'), ('کامل شده', 'کامل شده'), ('کنسل شده', 'کنسل شده'), ('درحال انتظار', 'درحال انتظار'), ('ارسال شده', 'ارسال شده'), ('تحویل شده', 'تحویل شده'), ('درحال بسته بندی', 'درحال بسته بندی'), ('پذیرفته شده', 'پذیرفته شده'), ('بسته بندی شده', 'بسته بندی شده'), ('معلق', 'معلق'), ('تایید مشتری', 'تایید مشتری')], default='معلق', max_length=50, verbose_name='وضعیت بسته')),
                ('count_of_packs', models.IntegerField(default=1, verbose_name='تعداد پاکت')),
                ('ship_fee', models.IntegerField(verbose_name='هزینه ارسال')),
                ('address', models.CharField(max_length=200, verbose_name='آدرس تحویل')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')),
                ('accept_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پذیرش')),
                ('pack_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ بسته بندی')),
                ('ship_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ حمل')),
                ('deliver_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ تحویل')),
                ('cancel_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انصراف')),
                ('no_ship', models.BooleanField(default=False, verbose_name='خودم تحویل میگیرم')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.customer', verbose_name='مشتری')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'سفارش ها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_home', models.BooleanField(default=False, verbose_name='نمایش در صفحه خانه')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='درصد تخفیف')),
                ('is_new', models.BooleanField(default=False, verbose_name='جدید است؟')),
                ('image', models.ImageField(blank=True, null=True, upload_to='market/images/Product/', verbose_name='تصویر 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='market/images/Product/', verbose_name='تصویر 2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='market/images/Product/', verbose_name='تصویر 3')),
                ('name', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('model_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='مدل')),
                ('barcode', models.CharField(blank=True, max_length=1000, null=True, verbose_name='بارکد')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('priority', models.IntegerField(default=1000, verbose_name='ترتیب')),
                ('origin_price', models.IntegerField(default=0, verbose_name='قیمت بدون تخفیف')),
                ('short_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='شرح کوتاه')),
                ('description', models.CharField(blank=True, default='', max_length=5000, null=True, verbose_name='شرح کامل')),
                ('tag', models.CharField(blank=True, max_length=50, null=True, verbose_name='برچسب')),
                ('time_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('time_updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ اصلاح')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='market/images/Product/thumbnail/', verbose_name='تصویر کوچک')),
                ('adder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.profile')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brand', to='market.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='market.category')),
                ('comments', models.ManyToManyField(blank=True, to='app.Comment', verbose_name='نظرات کاربرات')),
                ('related', models.ManyToManyField(blank=True, to='market.Product', verbose_name='related')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'کالا ها و محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='واحد فروش')),
                ('priority', models.IntegerField(default=1000, verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'ProductUnit',
                'verbose_name_plural': 'واحد فروش کالا ها',
            },
        ),
        migrations.CreateModel(
            name='ShopRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('خواف', 'خواف'), ('نشتیفان', 'نشتیفان'), ('سنگان', 'سنگان'), ('قاسم آباد', 'قاسم آباد'), ('تایباد', 'تایباد'), ('تربت جام', 'تربت جام'), ('فریمان', 'فریمان'), ('مشهد', 'مشهد'), ('تهران', 'تهران'), ('تربت حیدریه', 'تربت حیدریه')], default='خواف', max_length=50, verbose_name='نام شهر')),
                ('server_address', models.CharField(max_length=50, verbose_name='آدرس سرور')),
            ],
            options={
                'verbose_name': 'ShopRegion',
                'verbose_name_plural': 'منطقه های فروش',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='پیش عنوان')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='عنوان')),
                ('show', models.BooleanField(default=False, verbose_name='نمایش داده شود؟')),
                ('is_verified', models.BooleanField(default=False, verbose_name='تایید شده؟')),
                ('priority', models.IntegerField(default=1000, verbose_name='اولویت')),
                ('location', models.CharField(blank=True, max_length=1200, verbose_name='موقعیت')),
                ('body', models.CharField(blank=True, max_length=5000, verbose_name='متن')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='market/images/Supplier/', verbose_name='تصویر')),
                ('video_title', models.CharField(blank=True, max_length=100, verbose_name='عنوان ویدیو')),
                ('video_link', models.CharField(blank=True, max_length=1000, verbose_name='لینک ویدیو')),
                ('ship_fee', models.IntegerField(default=0, verbose_name='هزینه ارسال بسته')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس')),
                ('tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='تلفن')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.profile', verbose_name='profile')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.region', verbose_name='region')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'فروشگاه ها',
            },
        ),
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='market.employee')),
            ],
            options={
                'verbose_name': 'Accountant',
                'verbose_name_plural': 'حسابداران',
            },
            bases=('market.employee',),
        ),
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='market.employee')),
            ],
            options={
                'verbose_name': 'Cashier',
                'verbose_name_plural': 'صندوقدار ها',
            },
            bases=('market.employee',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='market.employee')),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'مدیر ها',
            },
            bases=('market.employee',),
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام انبار')),
                ('address', models.CharField(max_length=100, verbose_name='آدرس')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.supplier', verbose_name='فروشگاه')),
            ],
            options={
                'verbose_name': 'WareHouse',
                'verbose_name_plural': 'انبار های کالا',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(default='عدد', max_length=50, verbose_name='واحد فروش')),
                ('price', models.IntegerField(default=0, verbose_name='قیمت')),
                ('available', models.IntegerField(default=60, verbose_name='تعداد موجودی')),
                ('time_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت پیشنهاد')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product', verbose_name='محصول انتخابی')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.supplier', verbose_name='فروشگاه')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'کالاهای آماده فروش',
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='نام موسسه')),
                ('is_verified', models.BooleanField(default=False, verbose_name='تایید شده؟')),
                ('priority', models.IntegerField(default=1000, verbose_name='اولویت')),
                ('location', models.CharField(blank=True, max_length=1200, verbose_name='موقعیت')),
                ('body', models.CharField(blank=True, max_length=5000, verbose_name='متن')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='market/images/Supplier/', verbose_name='تصویر')),
                ('video_title', models.CharField(blank=True, max_length=100, verbose_name='عنوان ویدیو')),
                ('video_link', models.CharField(blank=True, max_length=1000, verbose_name='لینک ویدیو')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس')),
                ('tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='تلفن')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.profile', verbose_name='profile')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.region', verbose_name='region')),
            ],
            options={
                'verbose_name': 'Shipper',
                'verbose_name_plural': 'پیک های ارسال کالا',
            },
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام ویژگی')),
                ('value', models.CharField(max_length=50, verbose_name='مقدار ویژگی')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product')),
            ],
            options={
                'verbose_name': 'ProductSpecification',
                'verbose_name_plural': 'ProductSpecifications',
            },
        ),
        migrations.CreateModel(
            name='ProductInStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='تعداد')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
                ('adder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.employee', verbose_name='ثبت کننده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.product', verbose_name='کالا')),
                ('unit_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.productunit', verbose_name='واحد')),
                ('ware_house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.warehouse', verbose_name='انبار')),
            ],
            options={
                'verbose_name': 'ProductInStock',
                'verbose_name_plural': 'کالاهای موجود در انبار',
            },
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, verbose_name='نظر')),
                ('time_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ نظر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product', verbose_name=' محصول')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'ProductComment',
                'verbose_name_plural': 'نظر کاربران در مورد محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='unit_names',
            field=models.ManyToManyField(to='market.ProductUnit', verbose_name='واحد های قابل فروش'),
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('quantity', models.IntegerField(verbose_name='تعداد')),
                ('unit_name', models.CharField(max_length=50, verbose_name='واحد')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.order', verbose_name='فاکتور')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'OrderLine',
                'verbose_name_plural': 'ریز سفارش ها',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='market.shipper', verbose_name='پیک'),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.supplier', verbose_name='فروشگاه'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employer_shipper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.shipper', verbose_name='shipper'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employer_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.supplier', verbose_name='supplier'),
        ),
        migrations.AddField(
            model_name='employee',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.profile', verbose_name='profile'),
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('خانه', 'خانه'), ('محل کار', 'محل کار'), ('اداره', 'اداره'), ('شرکت', 'شرکت'), ('باغ', 'باغ')], default='خانه', max_length=100, verbose_name='عنوان')),
                ('agent', models.CharField(max_length=100, verbose_name='تحویل گیرنده')),
                ('street', models.CharField(max_length=100, verbose_name='آدرس')),
                ('tel', models.CharField(max_length=100, verbose_name='تلفن')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.customer', verbose_name='مشتری')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.region', verbose_name='region')),
            ],
            options={
                'verbose_name': 'DeliveryAddress',
                'verbose_name_plural': 'آدرس های تحویل',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='favorites',
            field=models.ManyToManyField(blank=True, to='market.Product', verbose_name='favorites'),
        ),
        migrations.AddField(
            model_name='customer',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.profile', verbose_name='profile'),
        ),
        migrations.CreateModel(
            name='CartLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='تعداد')),
                ('time_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درخواست')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.customer', verbose_name='مشتری')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.shop', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'CartLine',
                'verbose_name_plural': 'سبد های خرید',
            },
        ),
        migrations.CreateModel(
            name='WareHouseKeeper',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='market.employee')),
                ('ware_house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='market.warehouse', verbose_name='انبار')),
            ],
            options={
                'verbose_name': 'WareHouseKeeper',
                'verbose_name_plural': 'انباردار ها',
            },
            bases=('market.employee',),
        ),
    ]
