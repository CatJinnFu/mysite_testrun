# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0040_auto_20161129_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default='11/28/2016'),
        ),
    ]
