# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 03:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0060_auto_20161130_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 3, 46, 12, 646446, tzinfo=utc)),
        ),
    ]
