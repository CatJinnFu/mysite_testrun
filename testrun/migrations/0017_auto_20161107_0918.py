# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 22:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0016_auto_20161107_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='Processed',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 6, 22, 18, 9, 799928, tzinfo=utc)),
        ),
    ]