# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-06 11:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0027_auto_20180706_1357'),
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
