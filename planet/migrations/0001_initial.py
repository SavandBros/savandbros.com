# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields
import colorfield.fields
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='planet_coverplugin', parent_link=True, to='cms.CMSPlugin')),
                ('title', models.CharField(verbose_name='title', max_length=250, blank=True, null=True)),
                ('sub_title', models.CharField(verbose_name='sub title', max_length=500, blank=True, null=True)),
                ('detail', djangocms_text_ckeditor.fields.HTMLField(verbose_name='detail', blank=True, null=True)),
                ('image', filer.fields.image.FilerImageField(verbose_name='image', blank=True, null=True, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='MoneyCurrency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(verbose_name='code', max_length=3, unique=True, choices=[('AED', 'AED'), ('ALL', 'ALL'), ('AMD', 'AMD'), ('ANG', 'ANG'), ('AOA', 'AOA'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('AWG', 'AWG'), ('AZN', 'AZN'), ('BAM', 'BAM'), ('BBD', 'BBD'), ('BDT', 'BDT'), ('BGN', 'BGN'), ('BHD', 'BHD'), ('BND', 'BND'), ('BOB', 'BOB'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('BTN', 'BTN'), ('BWP', 'BWP'), ('BYR', 'BYR'), ('BZD', 'BZD'), ('CAD', 'CAD'), ('CHF', 'CHF'), ('CLP', 'CLP'), ('CNY', 'CNY'), ('COP', 'COP'), ('CRC', 'CRC'), ('CZK', 'CZK'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('DZD', 'DZD'), ('EGP', 'EGP'), ('ETB', 'ETB'), ('EUR', 'EUR'), ('FJD', 'FJD'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('GHS', 'GHS'), ('GMD', 'GMD'), ('GTQ', 'GTQ'), ('GYD', 'GYD'), ('HKD', 'HKD'), ('HNL', 'HNL'), ('HRK', 'HRK'), ('HUF', 'HUF'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('INR', 'INR'), ('ISK', 'ISK'), ('JEP', 'JEP'), ('JMD', 'JMD'), ('JOD', 'JOD'), ('JPY', 'JPY'), ('KES', 'KES'), ('KGS', 'KGS'), ('KHR', 'KHR'), ('KRW', 'KRW'), ('KWD', 'KWD'), ('KYD', 'KYD'), ('KZT', 'KZT'), ('LBP', 'LBP'), ('LKR', 'LKR'), ('LTL', 'LTL'), ('LVL', 'LVL'), ('MAD', 'MAD'), ('MDL', 'MDL'), ('MGA', 'MGA'), ('MKD', 'MKD'), ('MMK', 'MMK'), ('MNT', 'MNT'), ('MOP', 'MOP'), ('MUR', 'MUR'), ('MVR', 'MVR'), ('MXN', 'MXN'), ('MYR', 'MYR'), ('MZN', 'MZN'), ('NAD', 'NAD'), ('NGN', 'NGN'), ('NIO', 'NIO'), ('NOK', 'NOK'), ('NPR', 'NPR'), ('NZD', 'NZD'), ('OMR', 'OMR'), ('PEN', 'PEN'), ('PGK', 'PGK'), ('PHP', 'PHP'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('QAR', 'QAR'), ('RON', 'RON'), ('RSD', 'RSD'), ('RUB', 'RUB'), ('RWF', 'RWF'), ('SAR', 'SAR'), ('SCR', 'SCR'), ('SEK', 'SEK'), ('SGD', 'SGD'), ('STD', 'STD'), ('SYP', 'SYP'), ('THB', 'THB'), ('TND', 'TND'), ('TRY', 'TRY'), ('TTD', 'TTD'), ('TWD', 'TWD'), ('TZS', 'TZS'), ('UAH', 'UAH'), ('UGX', 'UGX'), ('USD', 'USD'), ('UYU', 'UYU'), ('VEF', 'VEF'), ('VND', 'VND'), ('VUV', 'VUV'), ('WST', 'WST'), ('XAF', 'XAF'), ('XBT', 'XBT'), ('XCD', 'XCD'), ('XOF', 'XOF'), ('XPF', 'XPF'), ('ZAR', 'ZAR'), ('ZMW', 'ZMW')])),
                ('rate', models.DecimalField(verbose_name='rate', max_digits=25, decimal_places=6)),
            ],
            options={
                'verbose_name': 'Money Currency',
                'verbose_name_plural': 'Money Currencies',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('pricing_type', models.IntegerField(verbose_name='pricing type', choices=[(0, 'Hourly'), (2, 'Monthly'), (4, 'Quarterly'), (5, 'Semi-Annually'), (6, 'Annually'), (7, 'Biennially'), (8, 'Triennially')])),
                ('price', models.DecimalField(verbose_name='price', max_digits=10, decimal_places=6)),
                ('currencies', models.ManyToManyField(to='planet.MoneyCurrency')),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Prices',
                'ordering': ('pricing_type',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('slug', models.SlugField(verbose_name='slug', unique=True)),
                ('slug_en', models.SlugField(verbose_name='slug', unique=True, null=True)),
                ('slug_hi', models.SlugField(verbose_name='slug', unique=True, null=True)),
                ('slug_ru', models.SlugField(verbose_name='slug', unique=True, null=True)),
                ('name', models.CharField(verbose_name='name', max_length=50)),
                ('name_en', models.CharField(verbose_name='name', max_length=50, null=True)),
                ('name_hi', models.CharField(verbose_name='name', max_length=50, null=True)),
                ('name_ru', models.CharField(verbose_name='name', max_length=50, null=True)),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description')),
                ('description_en', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', null=True)),
                ('description_hi', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', null=True)),
                ('description_ru', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', null=True)),
                ('featured', models.BooleanField(verbose_name='featured')),
                ('in_stock', models.BooleanField(verbose_name='in stock', default=True)),
                ('info', models.CharField(verbose_name='info', max_length=250, blank=True, null=True)),
                ('info_en', models.CharField(verbose_name='info', max_length=250, blank=True, null=True)),
                ('info_hi', models.CharField(verbose_name='info', max_length=250, blank=True, null=True)),
                ('info_ru', models.CharField(verbose_name='info', max_length=250, blank=True, null=True)),
                ('label', models.CharField(verbose_name='label', max_length=100, blank=True, null=True)),
                ('label_en', models.CharField(verbose_name='label', max_length=100, blank=True, null=True)),
                ('label_hi', models.CharField(verbose_name='label', max_length=100, blank=True, null=True)),
                ('label_ru', models.CharField(verbose_name='label', max_length=100, blank=True, null=True)),
                ('order_link', models.URLField()),
                ('order_link_en', models.URLField(null=True)),
                ('order_link_hi', models.URLField(null=True)),
                ('order_link_ru', models.URLField(null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=50)),
                ('name_en', models.CharField(verbose_name='name', max_length=50, null=True)),
                ('name_hi', models.CharField(verbose_name='name', max_length=50, null=True)),
                ('name_ru', models.CharField(verbose_name='name', max_length=50, null=True)),
                ('slug', models.SlugField(verbose_name='slug', unique=True)),
                ('slug_en', models.SlugField(verbose_name='slug', unique=True, null=True)),
                ('slug_hi', models.SlugField(verbose_name='slug', unique=True, null=True)),
                ('slug_ru', models.SlugField(verbose_name='slug', unique=True, null=True)),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description')),
                ('description_en', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', null=True)),
                ('description_hi', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', null=True)),
                ('description_ru', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', null=True)),
            ],
            options={
                'verbose_name': 'Product Group',
                'verbose_name_plural': 'Product Groups',
            },
        ),
        migrations.CreateModel(
            name='ProductGroupPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='planet_productgroupplugin', parent_link=True, to='cms.CMSPlugin')),
                ('product_group', models.ForeignKey(to='planet.ProductGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=250)),
                ('name_en', models.CharField(verbose_name='name', max_length=250, null=True)),
                ('name_hi', models.CharField(verbose_name='name', max_length=250, null=True)),
                ('name_ru', models.CharField(verbose_name='name', max_length=250, null=True)),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
                ('description_en', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
                ('description_hi', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
                ('description_ru', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.CreateModel(
            name='SectionItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=250)),
                ('title_en', models.CharField(verbose_name='title', max_length=250, null=True)),
                ('title_hi', models.CharField(verbose_name='title', max_length=250, null=True)),
                ('title_ru', models.CharField(verbose_name='title', max_length=250, null=True)),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
                ('description_en', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
                ('description_hi', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
                ('description_ru', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
                ('icon', models.CharField(verbose_name='icon', max_length=25, blank=True, null=True, help_text='an Icon from our icon/font framework, for instance "fa fa-login"')),
                ('icon_color', colorfield.fields.ColorField(max_length=18, blank=True, null=True)),
                ('link', models.URLField(verbose_name='link', blank=True, null=True)),
                ('item_order', models.PositiveIntegerField(default=0)),
                ('image', filer.fields.image.FilerImageField(verbose_name='image', blank=True, null=True, to=settings.FILER_IMAGE_MODEL)),
                ('section', models.ForeignKey(related_name='items', to='planet.Section')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Section Items',
                'ordering': ('item_order',),
            },
        ),
        migrations.CreateModel(
            name='SectionPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='planet_sectionplugin', parent_link=True, to='cms.CMSPlugin')),
                ('template', models.CharField(verbose_name='template', max_length=100)),
                ('section', models.ForeignKey(to='planet.Section')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=50)),
                ('name_en', models.CharField(verbose_name='name', max_length=50, null=True)),
                ('name_hi', models.CharField(verbose_name='name', max_length=50, null=True)),
                ('name_ru', models.CharField(verbose_name='name', max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=100)),
                ('name_en', models.CharField(verbose_name='name', max_length=100, null=True)),
                ('name_hi', models.CharField(verbose_name='name', max_length=100, null=True)),
                ('name_ru', models.CharField(verbose_name='name', max_length=100, null=True)),
                ('bio', models.TextField(verbose_name='bio')),
                ('bio_en', models.TextField(verbose_name='bio', null=True)),
                ('bio_hi', models.TextField(verbose_name='bio', null=True)),
                ('bio_ru', models.TextField(verbose_name='bio', null=True)),
                ('date_joined', models.DateField(verbose_name='date joined')),
                ('picture', filer.fields.image.FilerImageField(verbose_name='image', blank=True, null=True, to=settings.FILER_IMAGE_MODEL)),
                ('team', models.ForeignKey(to='planet.Team')),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
                'ordering': ('date_joined',),
            },
        ),
        migrations.CreateModel(
            name='TeamMemberPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='planet_teammemberplugin', parent_link=True, to='cms.CMSPlugin')),
                ('team_member', models.ForeignKey(to='planet.TeamMember')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TeamPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='planet_teamplugin', parent_link=True, to='cms.CMSPlugin')),
                ('team', models.ForeignKey(to='planet.Team')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(to='planet.ProductGroup'),
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(to='planet.Product'),
        ),
    ]
