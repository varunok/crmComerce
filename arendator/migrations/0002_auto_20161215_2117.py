# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0001_initial'),
        ('facility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arendator',
            name='number_of_persons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a', blank=True, to='facility.TypeNumberOfPerson', null=True),
        ),
        migrations.AddField(
            model_name='arendator',
            name='repairs',
            field=models.ManyToManyField(to='facility.TypeRepairs', verbose_name='\u0420\u0435\u043c\u043e\u043d\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='arendator',
            name='rieltor',
            field=models.ManyToManyField(related_name='rielt', verbose_name='\u0420\u0438\u0435\u043b\u0442\u043e\u0440', to='arendator.UserFullName', blank=True),
        ),
        migrations.AddField(
            model_name='arendator',
            name='room',
            field=models.ManyToManyField(to='facility.TypeRooms', verbose_name='\u041a\u043e\u043c\u043d\u0430\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='arendator',
            name='type_building_data',
            field=models.ManyToManyField(to='facility.TypeFacility', verbose_name='\u0422\u0438\u043f \u043e\u0431\u044a\u0435\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='arendator',
            name='type_client',
            field=models.ForeignKey(related_name='t_client', blank=True, to='arendator.TypeClient', null=True),
        ),
        migrations.AddField(
            model_name='arendator',
            name='type_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u042d\u0442\u0430\u043f', blank=True, to='arendator.TypeStage', null=True),
        ),
        migrations.AddField(
            model_name='arendator',
            name='type_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435', blank=True, to='arendator.TypeState', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='arendator',
            unique_together=set([('name', 'phone_first')]),
        ),
    ]
