# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0008_auto_20161216_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressfacilitydata',
            name='availability',
            field=models.ManyToManyField(to='facility.TypeAvailability', verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='addressfacilitydata',
            name='under_that',
            field=models.ManyToManyField(to='facility.TypeUnderThat', verbose_name='\u041f\u043e\u0434 \u0427\u0442\u043e', blank=True),
        ),
    ]
