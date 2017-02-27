# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arendator', '0001_initial'),
        ('facility', '0001_initial'),
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowsArendator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('array_arendator', models.ForeignKey(to='arendator.Arendator', null=True)),
                ('array_cont_ower', models.ForeignKey(to='facility.ContactOwner', null=True)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043a\u0430\u0437 \u0430\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u0430\u043c',
                'verbose_name_plural': '\u041f\u043e\u043a\u0430\u0437\u0438 \u0430\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u0430\u043c',
            },
        ),
        migrations.CreateModel(
            name='ShowsBuyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('array_buyer', models.ForeignKey(to='buyer.Buyer', null=True)),
                ('array_cont_ower', models.ForeignKey(to='facility.ContactOwner', null=True)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043a\u0430\u0437 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044e',
                'verbose_name_plural': '\u041f\u043e\u043a\u0430\u0437\u0438 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f\u043c',
            },
        ),
        migrations.CreateModel(
            name='SingleObjComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9')),
                ('date_comment', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f')),
                ('author_comment', models.CharField(max_length=100, verbose_name='\u0410\u0432\u0442\u043e\u0440 \u043a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u044f')),
                ('image', models.CharField(default=b'0', max_length=100)),
                ('type_tabs', models.CharField(max_length=20, verbose_name='\u041a\u0430\u043a\u0430\u044f \u0432\u043a\u043b\u0430\u0434\u043a\u0430?')),
                ('obj_comments', models.ForeignKey(verbose_name='\u041e\u0431\u044c\u0435\u043a\u0442', to='facility.ContactOwner')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u043e\u0431\u0435\u043a\u0442\u0430',
                'verbose_name_plural': '\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Tie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tie_arenda', models.ManyToManyField(to='arendator.Arendator', verbose_name='\u0421\u0432\u044f\u0437\u043a\u0430 \u043e\u0431\u0435\u043a\u0442\u0430 \u0441 \u0430\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u043e\u043c', blank=True)),
                ('tie_cont_owner', models.OneToOneField(verbose_name='\u041e\u0431\u0435\u043a\u0442', to='facility.ContactOwner')),
            ],
            options={
                'verbose_name': '\u0421\u0432\u044f\u0437\u043a\u0430 \u0441 \u0430\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u043e\u043c',
                'verbose_name_plural': '\u0421\u0432\u044f\u0437\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='TieBuyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tie_buye', models.ManyToManyField(to='buyer.Buyer', verbose_name='\u0421\u0432\u044f\u0437\u043a\u0430 \u043e\u0431\u0435\u043a\u0442\u0430 \u0441 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u0435\u043c', blank=True)),
                ('tie_cont_owner', models.OneToOneField(verbose_name='\u041e\u0431\u0435\u043a\u0442', to='facility.ContactOwner')),
            ],
            options={
                'verbose_name': '\u0421\u0432\u044f\u0437\u043a\u0430 \u0441 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u0435\u043c',
                'verbose_name_plural': '\u0421\u0432\u044f\u0437\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='TypeShows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_shows', models.CharField(max_length=50, unique=True, null=True, verbose_name='\u0422\u0438\u043f \u043f\u043e\u043a\u0430\u0437\u0430')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043f\u043e\u043a\u0430\u0437\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u041f\u043e\u043a\u0430\u0437\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='showsbuyer',
            name='type_shows_buyer',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u043a\u0430\u0437\u0438 \u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044e', to='single_object.TypeShows', null=True),
        ),
        migrations.AddField(
            model_name='showsarendator',
            name='type_shows_arendator',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u043a\u0430\u0437\u0438 \u0410\u0440\u0435\u043d\u0434\u0430\u0442\u043e\u0440\u0430\u043c', to='single_object.TypeShows', null=True),
        ),
    ]
