# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-05 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0019_auto_20180705_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalmammalianline',
            name='document',
        ),
        migrations.RemoveField(
            model_name='mammalianline',
            name='document',
        ),
        migrations.DeleteModel(
            name='MammalianLineDoc',
        ),
    ]
