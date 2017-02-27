# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0002_auto_20161215_2117'),
        ('auth', '0006_require_contenttypes_0002'),
        ('facility', '0001_initial'),
        ('buyer', '0002_auto_20161215_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dead_line', models.DateTimeField(verbose_name='\u041a\u0440\u0430\u0439\u043d\u0438\u0439 \u0441\u0440\u043e\u043a')),
                ('task_text', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442', blank=True)),
                ('task_trash', models.BooleanField(default=False, verbose_name=b'\xd0\x92 \xd0\xba\xd0\xbe\xd1\x80\xd0\xb7\xd0\xb8\xd0\xbd\xd1\x83')),
                ('task_archiv', models.BooleanField(default=False, verbose_name=b'\xd0\x92 \xd0\xb0\xd1\x80\xd1\x85\xd0\xb8\xd0\xb2')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
            ],
            options={
                'ordering': ['dead_line'],
                'verbose_name': '\u0417\u0430\u0434\u0430\u0447\u0430',
                'verbose_name_plural': '\u0417\u0430\u0434\u0430\u0447\u0438',
            },
        ),
        migrations.CreateModel(
            name='TypeComplexity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complexity', models.CharField(max_length=20, null=True, verbose_name='\u0422\u0438\u043f \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438',
                'verbose_name_plural': '\u0422\u0438\u043f\u0438 \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='UserFullName',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='tasking',
            name='access',
            field=models.ManyToManyField(related_name='access', verbose_name='\u0414\u043e\u0441\u0442\u0443\u043f', to='tasking.UserFullName', blank=True),
        ),
        migrations.AddField(
            model_name='tasking',
            name='rieltor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0420\u0438\u0435\u043b\u0442\u043e\u0440', blank=True, to='tasking.UserFullName', null=True),
        ),
        migrations.AddField(
            model_name='tasking',
            name='task_arendator',
            field=models.ForeignKey(verbose_name='ID(A) \u0410\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440', blank=True, to='arendator.Arendator', null=True),
        ),
        migrations.AddField(
            model_name='tasking',
            name='task_buyer',
            field=models.ForeignKey(verbose_name='ID(P) \u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c', blank=True, to='buyer.Buyer', null=True),
        ),
        migrations.AddField(
            model_name='tasking',
            name='task_facility',
            field=models.ForeignKey(verbose_name='ID(O) \u041e\u0431\u044a\u0435\u043a\u0442', blank=True, to='facility.ContactOwner', null=True),
        ),
        migrations.AddField(
            model_name='tasking',
            name='type_complex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c', blank=True, to='tasking.TypeComplexity', null=True),
        ),
    ]
