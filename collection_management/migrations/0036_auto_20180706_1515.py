# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-06 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0035_auto_20180706_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalmammalianline',
            name='parental_line',
        ),
        migrations.RemoveField(
            model_name='mammalianline',
            name='parental_line',
        ),
    ]
