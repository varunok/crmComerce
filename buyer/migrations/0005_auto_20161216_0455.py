# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0009_auto_20161216_0353'),
        ('buyer', '0004_remove_buyer_number_of_persons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='floors_from',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='floors_to',
        ),
        migrations.AddField(
            model_name='buyer',
            name='entrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0412\u0445\u043e\u0434', to_field=b'entrances', blank=True, to='facility.TypeEntrance', null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435', to_field=b'locations', blank=True, to='facility.TypeLocations', null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='number_of_storeys',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u044c', to_field=b'storeys', blank=True, to='facility.TypeStoreys', null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='shopping_room_from',
            field=models.IntegerField(null=True, verbose_name='\u0422\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0437\u0430\u043b \u041e\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='shopping_room_to',
            field=models.IntegerField(null=True, verbose_name='\u0422\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0437\u0430\u043b \u0414\u043e', blank=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='under_that',
            field=models.ManyToManyField(to='facility.TypeUnderThat', verbose_name='\u041f\u043e\u0434 \u0447\u0442\u043e?', blank=True),
        ),
    ]
