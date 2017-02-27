# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('youtube', models.CharField(max_length=500, verbose_name='\u0412\u0438\u0434\u0435\u043e')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435',
            },
        ),
    ]
