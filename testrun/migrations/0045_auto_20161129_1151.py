# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 00:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0044_auto_20161129_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 29, 0, 51, 30, 183522, tzinfo=utc)),
        ),
    ]
