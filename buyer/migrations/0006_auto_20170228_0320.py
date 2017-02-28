# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0010_addressfacilitydata_literal'),
        ('arendator', '0006_auto_20170228_0313'),
        ('buyer', '0005_auto_20161216_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='entrance',
        ),
        migrations.AddField(
            model_name='buyer',
            name='entrance',
            field=models.ManyToManyField(to='facility.TypeEntrance', verbose_name='\u0412\u0445\u043e\u0434', blank=True),
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='location',
        ),
        migrations.AddField(
            model_name='buyer',
            name='location',
            field=models.ManyToManyField(to='facility.TypeLocations', verbose_name='\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='number_of_storeys',
        ),
        migrations.AddField(
            model_name='buyer',
            name='number_of_storeys',
            field=models.ManyToManyField(to='facility.TypeStoreys', verbose_name='\u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u044c', blank=True),
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='type_stage',
        ),
        migrations.AddField(
            model_name='buyer',
            name='type_stage',
            field=models.ManyToManyField(to='arendator.TypeStage', verbose_name='\u042d\u0442\u0430\u043f', blank=True),
        ),
    ]
