# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0002_auto_20161215_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arendator',
            name='room',
        ),
    ]
