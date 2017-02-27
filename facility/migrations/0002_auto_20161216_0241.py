# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeLocations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locations', models.CharField(max_length=50, unique=True, null=True, verbose_name='\u0422\u0438\u043f \u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435', to_field=b'locations', blank=True, to='facility.TypeLocations', null=True),
        ),
    ]
