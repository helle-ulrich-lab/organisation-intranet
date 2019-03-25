# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-06 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0030_auto_20180706_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmammalianline',
            name='parental_line',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='collection_management.HistoricalMammalianLine'),
        ),
        migrations.AddField(
            model_name='mammalianline',
            name='parental_line',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='collection_management.MammalianLine'),
            preserve_default=False,
        ),
    ]
