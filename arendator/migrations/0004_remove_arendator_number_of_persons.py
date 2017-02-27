# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0003_remove_arendator_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arendator',
            name='number_of_persons',
        ),
    ]
