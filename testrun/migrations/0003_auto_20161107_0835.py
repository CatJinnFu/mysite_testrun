# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 21:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0002_auto_20161105_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 6, 21, 35, 7, 565636, tzinfo=utc)),
        ),
    ]
