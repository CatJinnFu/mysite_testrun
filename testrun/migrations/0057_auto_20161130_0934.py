# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 22:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testrun', '0056_auto_20161130_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card_type',
            old_name='card_type',
            new_name='type',
        ),
    ]