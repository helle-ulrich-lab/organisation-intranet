# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-11 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0054_auto_20190410_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalhuplasmid',
            name='name',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='huplasmid',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='huplasmid',
            name='plasmid_map',
            field=models.FileField(blank=True, upload_to='collection_management/huplasmid/dna/', verbose_name='Plasmid map (max. 2 MB)'),
        ),
    ]
