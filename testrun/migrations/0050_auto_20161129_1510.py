# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 04:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0049_auto_20161129_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 29, 15, 10, 35, 87971)),
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_transaction',
            field=models.CharField(default=datetime.datetime(2016, 11, 29, 15, 10, 35, 87971), max_length=200),
        ),
    ]
