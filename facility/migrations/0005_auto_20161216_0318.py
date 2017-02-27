# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0004_auto_20161216_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDocumentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documentations', models.CharField(max_length=50, unique=True, null=True, verbose_name='\u0422\u0438\u043f \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432',
            },
        ),
        migrations.AlterField(
            model_name='addressfacilitydata',
            name='rooms',
            field=models.CharField(max_length=200, null=True, verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='addressfacilitydata',
            name='documentation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b', to_field=b'documentations', blank=True, to='facility.TypeDocumentation', null=True),
        ),
    ]
