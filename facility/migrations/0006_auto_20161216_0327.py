# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0003_remove_arendator_room'),
        ('buyer', '0003_remove_buyer_room'),
        ('facility', '0005_auto_20161216_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='area_badroom',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='area_extra_room',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='area_kitchen',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='area_living_room',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='first_floor',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='floor',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='floors_up',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='last_floor',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='number_of_floors',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='room',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='total_area',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='type_building_data',
        ),
        migrations.DeleteModel(
            name='TypeBuilding',
        ),
        migrations.DeleteModel(
            name='TypeRooms',
        ),
    ]
