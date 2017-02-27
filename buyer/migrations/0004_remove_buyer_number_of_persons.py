# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_remove_buyer_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='number_of_persons',
        ),
    ]
