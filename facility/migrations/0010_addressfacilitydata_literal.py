# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0009_auto_20161216_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressfacilitydata',
            name='literal',
            field=models.CharField(max_length=10, null=True, verbose_name='\u0411\u0443\u043a\u0432\u0435\u043d\u043d\u044b\u0439 \u0438\u043d\u0434\u0435\u043a\u0441', blank=True),
        ),
    ]
