# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 22:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0052_auto_20161129_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 29, 22, 19, 37, 631673, tzinfo=utc)),
        ),
    ]
