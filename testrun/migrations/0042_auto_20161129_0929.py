# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0041_auto_20161129_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default='28/11/2016'),
        ),
    ]