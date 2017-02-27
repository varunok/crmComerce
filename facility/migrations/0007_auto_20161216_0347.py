# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0006_auto_20161216_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeAvailability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('availabilitys', models.CharField(max_length=50, unique=True, null=True, verbose_name='\u0422\u0438\u043f \u041d\u0430\u043b\u0438\u0447\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u041d\u0430\u043b\u0438\u0447\u0438\u0435',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u041d\u0430\u043b\u0438\u0447\u0438\u0435',
            },
        ),
        migrations.CreateModel(
            name='TypeUnderThat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('under_thats', models.CharField(max_length=50, unique=True, null=True, verbose_name='\u0422\u0438\u043f \u041f\u043e\u0434 \u0447\u0442\u043e', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u041f\u043e\u0434 \u0447\u0442\u043e',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u041f\u043e\u0434 \u0447\u0442\u043e',
            },
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='furniture',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='lavatory',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='number_of_persons',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='prepayment',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='sleeps',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='the_presence_of_hot_water',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='where_to_stay',
        ),
        migrations.RemoveField(
            model_name='addressfacilitydata',
            name='windows',
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='availability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435', blank=True, to='facility.TypeAvailability', null=True),
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='under_that',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u041f\u043e\u0434 \u0427\u0442\u043e', blank=True, to='facility.TypeUnderThat', null=True),
        ),
    ]
