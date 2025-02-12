# Generated by Django 3.2.4 on 2021-06-11 03:46

import colorfield.fields
import django.contrib.contenttypes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('admin_index', '0001_initial'), ('admin_index', '0002_auto_20170802_1754'), ('admin_index', '0003_auto_20200724_1516'), ('admin_index', '0004_auto_20210611_0142'), ('admin_index', '0005_auto_20210611_0144'), ('admin_index', '0006_theme'), ('admin_index', '0007_rename_dm_i_c_theme_dm_c')]

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentTypeProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'ordering': ('app_label', 'model'),
            },
            bases=('contenttypes.contenttype',),
            managers=[
                ('objects', django.contrib.contenttypes.models.ContentTypeManager()),
            ],
        ),
        migrations.CreateModel(
            name='AppGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('models', models.ManyToManyField(blank=True, to='admin_index.ContentTypeProxy')),
                ('icon', models.FileField(blank=True, upload_to='', verbose_name='icon')),
            ],
            options={
                'verbose_name_plural': 'application groups',
                'verbose_name': 'application group',
                'abstract': False,
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='AppLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('app_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_index.appgroup')),
                ('icon', models.FileField(blank=True, upload_to='', verbose_name='icon')),
            ],
            options={
                'verbose_name_plural': 'application links',
                'verbose_name': 'application link',
                'abstract': False,
                'ordering': ('order',),
                'unique_together': {('app_group', 'link')},
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Theme name')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('dm_bc', colorfield.fields.ColorField(default='#417690', max_length=18, verbose_name='.dropdown-menu background color')),
                ('dm_hover_bc', colorfield.fields.ColorField(default='#79aec8', max_length=18, verbose_name='.dropdown-menu:hover background color')),
                ('dm_c', colorfield.fields.ColorField(default='#fff', max_length=18, verbose_name='.dropdown-menu item color')),
                ('dm_drop_bc', colorfield.fields.ColorField(default='#417690', max_length=18, verbose_name='.dropdown-menu__drop:hover background color')),
                ('dm_drop_hover_bc', colorfield.fields.ColorField(default='#79aec8', max_length=18, verbose_name='.dropdown-menu__drop background color')),
                ('dm_drop_c', colorfield.fields.ColorField(default='#fff', max_length=18, verbose_name='.dropdown-menu__drop color')),
            ],
            options={
                'verbose_name': 'design theme',
                'verbose_name_plural': 'design themes',
            },
        ),
    ]
