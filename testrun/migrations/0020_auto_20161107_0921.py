# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 22:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0019_auto_20161107_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 6, 22, 21, 22, 443146, tzinfo=utc)),
        ),
    ]
