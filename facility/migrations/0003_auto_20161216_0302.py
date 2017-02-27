# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_auto_20161216_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeStoreys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storeys', models.CharField(max_length=50, unique=True, null=True, verbose_name='\u0422\u0438\u043f \u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u0438',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='footage',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\u041c\u0435\u0442\u0440\u0430\u0436', blank=True),
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='shopping_room',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\u0422\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0437\u0430\u043b', blank=True),
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='number_of_storeys',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u042d\u0442\u0430\u0436\u043d\u043e\u0441\u0442\u044c', to_field=b'storeys', blank=True, to='facility.TypeStoreys', null=True),
        ),
    ]
