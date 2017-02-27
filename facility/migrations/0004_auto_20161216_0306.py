# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0003_auto_20161216_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeEntrance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrances', models.CharField(max_length=50, unique=True, null=True, verbose_name='\u0422\u0438\u043f \u0412\u0445\u043e\u0434\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0412\u0445\u043e\u0434\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0412\u0445\u043e\u0434\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='entrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0412\u0445\u043e\u0434', to_field=b'entrances', blank=True, to='facility.TypeEntrance', null=True),
        ),
    ]
