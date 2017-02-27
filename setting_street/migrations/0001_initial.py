# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('district', models.CharField(unique=True, max_length=50, verbose_name='\u0420\u0430\u0439\u043e\u043d')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0439\u043e\u043d',
                'verbose_name_plural': '\u0420\u0430\u0439\u043e\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=50, verbose_name='\u0423\u043b\u0438\u0446\u0430')),
                ('full_street', models.CharField(max_length=80, unique=True, null=True, verbose_name='\u0423\u043b\u0438\u0446\u0430(\u043f\u043e\u043b\u043d.)')),
            ],
            options={
                'verbose_name': '\u0423\u043b\u0438\u0446\u0430',
                'verbose_name_plural': '\u0423\u043b\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='Subway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subway', models.CharField(unique=True, max_length=50, verbose_name='\u041c\u0435\u0442\u0440\u043e')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0442\u0440\u043e',
                'verbose_name_plural': '\u041c\u0435\u0442\u0440\u043e',
            },
        ),
        migrations.CreateModel(
            name='TypesStreet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_street', models.CharField(max_length=30, verbose_name='\u0422\u0438\u043f \u0443\u043b\u0438\u0446\u044b')),
                ('short_name', models.CharField(max_length=30, verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0443\u043b\u0438\u0446\u044b',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0443\u043b\u0438\u0446',
            },
        ),
        migrations.AddField(
            model_name='street',
            name='type_street_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0422\u0438\u043f \u0443\u043b\u0438\u0446\u044b', to='setting_street.TypesStreet', null=True),
        ),
    ]
