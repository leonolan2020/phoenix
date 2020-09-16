# Generated by Django 3.1 on 2020-09-16 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0003_auto_20200915_1352'),
        ('market', '0002_auto_20200917_0213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0, verbose_name='rank')),
                ('role', models.CharField(choices=[('پیش فرض', 'پیش فرض'), ('حسابدار', 'حسابدار'), ('مدیریت', 'مدیریت'), ('راننده', 'راننده'), ('متخصص', 'متخصص'), ('مهندس', 'مهندس')], default='پیش فرض', max_length=50, verbose_name='پست سازمانی')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'PurchaseAgent',
                'verbose_name_plural': 'مامور',
            },
        ),
        migrations.CreateModel(
            name='WorkUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('حسابداری', 'حسابداری'), ('مدیریت', 'مدیریت'), ('حمل و نقل', 'حمل و نقل'), ('کارپردازی', 'کارپردازی'), ('عمران', 'عمران'), ('تاسیسات', 'تاسیسات'), ('مهندسی', 'مهندسی')], default='حسابداری', max_length=50, verbose_name='title')),
                ('icon', models.CharField(choices=[('account_circle', 'account_circle'), ('add_shopping_cart', 'add_shopping_cart'), ('alarm', 'alarm'), ('attach_file', 'attach_file'), ('attach_money', 'attach_money'), ('backup', 'backup'), ('build', 'build'), ('chat', 'chat'), ('dashboard', 'dashboard'), ('delete', 'delete'), ('description', 'description'), ('face', 'face'), ('favorite', 'favorite'), ('get_app', 'get_app'), ('help_outline', 'help_outline'), ('home', 'home'), ('important_devices', 'important_devices'), ('link', 'link'), ('local_shipping', 'local_shipping'), ('lock', 'lock'), ('mail', 'mail'), ('notification_important', 'notification_important'), ('psychology', 'psychology'), ('publish', 'publish'), ('reply', 'reply'), ('schedule', 'schedule'), ('send', 'send'), ('settings', 'settings'), ('share', 'share'), ('sync', 'sync'), ('vpn_key', 'vpn_key')], default='link', max_length=50, verbose_name='icon')),
                ('color', models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose')], default='primary', max_length=50, verbose_name='color')),
                ('agents', models.ManyToManyField(blank=True, to='automation.Agent', verbose_name='agents')),
            ],
            options={
                'verbose_name': 'WorkUnit',
                'verbose_name_plural': 'واحد های سازمانی',
            },
        ),
        migrations.CreateModel(
            name='PurchaseAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0, verbose_name='rank')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'PurchaseAgent',
                'verbose_name_plural': 'PurchaseAgents',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ourwork_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ourwork')),
                ('warehouses', models.ManyToManyField(blank=True, to='market.WareHouse', verbose_name='warehouses')),
                ('work_units', models.ManyToManyField(blank=True, to='automation.WorkUnit', verbose_name='work_units')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=('app.ourwork',),
        ),
        migrations.CreateModel(
            name='ProductRequestSignature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('پذیرفته شده', 'پذیرفته شده'), ('رد شده', 'رد شده'), ('درخواست شده', 'درخواست شده'), ('در حال انجام', 'در حال انجام'), ('در حال پردازش', 'در حال پردازش'), ('لغو شده', 'لغو شده'), ('کامل شده', 'کامل شده')], default='درخواست شده', max_length=50, verbose_name='status')),
                ('signature', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.signature', verbose_name='signatures')),
            ],
            options={
                'verbose_name': 'ProductRequestSignature',
                'verbose_name_plural': 'ProductRequestSignatures',
            },
        ),
        migrations.CreateModel(
            name='ProductRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('status', models.CharField(choices=[('پذیرفته شده', 'پذیرفته شده'), ('رد شده', 'رد شده'), ('درخواست شده', 'درخواست شده'), ('در حال انجام', 'در حال انجام'), ('در حال پردازش', 'در حال پردازش'), ('لغو شده', 'لغو شده'), ('کامل شده', 'کامل شده')], default='درخواست شده', max_length=50, verbose_name='status')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product', verbose_name='product')),
                ('product_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.productunit', verbose_name='product_unit')),
                ('purchase_agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='automation.purchaseagent', verbose_name='purchase_agent')),
                ('signatures', models.ManyToManyField(blank=True, to='automation.ProductRequestSignature', verbose_name='signatures')),
                ('work_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation.workunit', verbose_name='واحد سازمانی')),
            ],
            options={
                'verbose_name': 'ProductRequest',
                'verbose_name_plural': 'ProductRequests',
            },
        ),
        migrations.CreateModel(
            name='LetterSignature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('پیش نویس', 'پیش نویس'), ('پذیرفته شده', 'پذیرفته شده'), ('رد شده', 'رد شده'), ('درخواست شده', 'درخواست شده'), ('در حال انجام', 'در حال انجام'), ('در حال پردازش', 'در حال پردازش'), ('لغو شده', 'لغو شده'), ('کامل شده', 'کامل شده')], default='پیش نویس', max_length=50, verbose_name='status')),
                ('signature', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.signature', verbose_name='signatures')),
            ],
            options={
                'verbose_name': 'LetterSignature',
                'verbose_name_plural': 'LetterSignatures',
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('body', models.CharField(max_length=50, verbose_name='body')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date_added')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='فرستنده')),
                ('signatures', models.ManyToManyField(blank=True, to='automation.LetterSignature', verbose_name='signatures')),
                ('work_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automation.workunit', verbose_name='گیرنده')),
            ],
            options={
                'verbose_name': 'Letter',
                'verbose_name_plural': 'Letters',
            },
        ),
    ]
