# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='T\u0435\u043a\u0441\u0442 \u041d\u043e\u0442\u0430\u0442\u043a\u0438')),
                ('name', models.CharField(max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f')),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0442\u0430\u0442\u043a\u0430',
                'verbose_name_plural': '\u041d\u043e\u0442\u0430\u0442\u043a\u0438',
            },
        ),
    ]
