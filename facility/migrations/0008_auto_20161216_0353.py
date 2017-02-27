# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0004_remove_arendator_number_of_persons'),
        ('buyer', '0004_remove_buyer_number_of_persons'),
        ('facility', '0007_auto_20161216_0347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TypeEquipment',
        ),
        migrations.DeleteModel(
            name='TypeFurniture',
        ),
        migrations.DeleteModel(
            name='TypeLavatory',
        ),
        migrations.DeleteModel(
            name='TypeNumberOfPerson',
        ),
        migrations.DeleteModel(
            name='TypePrepayment',
        ),
        migrations.DeleteModel(
            name='TypeThePresenceOfHotWater',
        ),
        migrations.DeleteModel(
            name='TypeWhereToStay',
        ),
        migrations.DeleteModel(
            name='TypeWindows',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='availability',
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='availability',
            field=models.ManyToManyField(to='facility.TypeAvailability', null=True, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435', blank=True),
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='under_that',
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='under_that',
            field=models.ManyToManyField(to='facility.TypeUnderThat', null=True, verbose_name='\u041f\u043e\u0434 \u0427\u0442\u043e', blank=True),
        ),
    ]
