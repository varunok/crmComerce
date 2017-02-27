# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import arendator.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('setting_street', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arendator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commission', models.CharField(max_length=10, null=True, verbose_name='\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f', blank=True)),
                ('name', models.CharField(max_length=250, null=True, verbose_name='\u0418\u043c\u044f')),
                ('phone_first', models.CharField(max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d - 1', validators=[arendator.models.validate_isnumber])),
                ('phone_second', models.CharField(blank=True, max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d - 2', validators=[arendator.models.validate_isnumber])),
                ('comment', models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u0415\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430', blank=True)),
                ('rooms_from', models.IntegerField(null=True, verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442 \u041e\u0442', blank=True)),
                ('rooms_to', models.IntegerField(null=True, verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442 \u0414\u043e', blank=True)),
                ('floors_from', models.IntegerField(null=True, verbose_name='\u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u044c \u041e\u0442', blank=True)),
                ('floors_to', models.IntegerField(null=True, verbose_name='\u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u044c \u0414\u043e', blank=True)),
                ('area_from', models.IntegerField(null=True, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u041e\u0442', blank=True)),
                ('area_to', models.IntegerField(null=True, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u0414\u043e', blank=True)),
                ('price_from', models.IntegerField(null=True, verbose_name='\u0426\u0435\u043d\u0430 \u041e\u0442', blank=True)),
                ('price_to', models.IntegerField(null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0414\u043e', blank=True)),
                ('date_term', models.DateField(null=True, verbose_name='\u0421\u0440\u043e\u043a\u0438', blank=True)),
                ('review_date', models.DateField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f', null=True)),
                ('call_date', models.DateField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0437\u0432\u043e\u043d\u043a\u0430', blank=True)),
                ('time_trash', models.DateTimeField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f', blank=True)),
                ('name_user_trash', models.CharField(max_length=100, null=True, verbose_name='\u041a\u0442\u043e \u0443\u0434\u0430\u043b\u0438\u043b', blank=True)),
                ('trash', models.BooleanField(default=False, verbose_name='\u041a\u043e\u0440\u0437\u0438\u043d\u0430')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('district_obj', models.ManyToManyField(related_name='districts', verbose_name='\u0420\u0430\u0439\u043e\u043d', to='setting_street.District', blank=True)),
            ],
            options={
                'verbose_name': '\u0410\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440',
                'verbose_name_plural': '\u0410\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u0438',
            },
        ),
        migrations.CreateModel(
            name='TypeClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.CharField(max_length=150, null=True, verbose_name='\u0422\u0438\u043f \u043a\u043b\u0438\u0435\u043d\u0442\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043a\u043b\u0438\u0435\u043d\u0442\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u0438 \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='TypeStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stage', models.CharField(max_length=150, null=True, verbose_name='\u0422\u0438\u043f \u042d\u0442\u0430\u043f\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u042d\u0442\u0430\u043f\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u0438 \u042d\u0442\u0430\u043f\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='TypeState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=150, null=True, verbose_name='\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f',
                'verbose_name_plural': '\u0422\u0438\u043f\u0438 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='UserFullName',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='arendator',
            name='loyality',
            field=models.ManyToManyField(related_name='loyal', verbose_name='\u041b\u043e\u044f\u043b\u044c\u043d\u043e\u0441\u0442\u044c', to='arendator.UserFullName', blank=True),
        ),
    ]
