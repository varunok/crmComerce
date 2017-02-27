# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('agency', models.CharField(max_length=30, null=True, verbose_name='\u0410\u0433\u0435\u043d\u0441\u0442\u0432\u043e', blank=True)),
                ('phone', models.CharField(max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('phone_second', models.CharField(max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d 2', blank=True)),
                ('phone_third', models.CharField(max_length=15, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d 3', blank=True)),
                ('site', models.URLField(null=True, verbose_name='\u0421\u0430\u0439\u0442', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email', blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041c\u0430\u043a\u043b\u0435\u0440',
                'verbose_name_plural': '\u041c\u0430\u043a\u043b\u0435\u0440\u0430',
            },
        ),
        migrations.CreateModel(
            name='TypeCooperations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_cooperation', models.CharField(max_length=50, verbose_name='\u0422\u0438\u043f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430',
            },
        ),
        migrations.CreateModel(
            name='TypeWhiteBlack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_white_black', models.CharField(max_length=50, verbose_name='\u0422\u0438\u043f \u043c\u0430\u043a\u043b\u0435\u0440\u0430')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043c\u0430\u043a\u043b\u0435\u0440\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u0438 \u043c\u0430\u043a\u043b\u0435\u0440\u043e\u0432',
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
            model_name='makler',
            name='cooperation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0422\u0438\u043f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430', blank=True, to='makler.TypeCooperations', null=True),
        ),
        migrations.AddField(
            model_name='makler',
            name='rieltor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0420\u0438\u0435\u043b\u0442\u043e\u0440', blank=True, to='makler.UserFullName', null=True),
        ),
        migrations.AddField(
            model_name='makler',
            name='white_black',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0422\u0438\u043f \u043c\u0430\u043a\u043b\u0435\u0440\u0430', to='makler.TypeWhiteBlack'),
        ),
    ]
