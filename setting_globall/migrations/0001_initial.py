# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Franshise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('franshise', models.CharField(max_length=100, null=True, verbose_name='\u0424\u0440\u0430\u043d\u0448\u0438\u0437\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u0424\u0440\u0430\u043d\u0448\u0438\u0437\u0430',
            },
        ),
        migrations.CreateModel(
            name='FranshiseSity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sity', models.CharField(max_length=100, null=True, verbose_name='\u0413\u043e\u0440\u043e\u0434', blank=True)),
            ],
            options={
                'verbose_name': '\u0413\u043e\u0440\u043e\u0434 \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0438',
            },
        ),
        migrations.CreateModel(
            name='ListNationalCarrency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency_glob', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u0421\u043f\u0438\u0441\u043e\u043a \u043d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0439 \u0432\u0430\u043b\u044e\u0442\u044b',
                'verbose_name_plural': '\u0421\u043f\u0438\u0441\u043a\u0438 \u043d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0439 \u0432\u0430\u043b\u044e\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='NationalCarrency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currency', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0439 \u0432\u0430\u043b\u044e\u0442\u044b',
                'verbose_name_plural': '\u0422\u0438\u043f \u043d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0439 \u0432\u0430\u043b\u044e\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c')),
                ('phone', models.CharField(max_length=50, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u043f\u0438\u0441\u044c',
                'verbose_name_plural': '\u041f\u043e\u0434\u043f\u0438\u0441\u044c',
            },
        ),
    ]
