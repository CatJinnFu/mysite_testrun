# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 21:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0003_auto_20161107_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=99999999),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 6, 21, 41, 14, 279897, tzinfo=utc)),
        ),
    ]