# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-12 09:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0059_auto_20190412_1125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalmammalianline',
            old_name='parental_line_new',
            new_name='parental_line',
        ),
        migrations.RenameField(
            model_name='mammalianline',
            old_name='parental_line_new',
            new_name='parental_line',
        ),
    ]