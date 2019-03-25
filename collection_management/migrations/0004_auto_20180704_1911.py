# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-04 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_management', '0003_auto_20180330_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmammalianline',
            name='parental_line',
            field=models.CharField(blank=True, max_length=255, verbose_name='Parental cell line'),
        ),
        migrations.AddField(
            model_name='mammalianline',
            name='parental_line',
            field=models.CharField(blank=True, max_length=255, verbose_name='Parental cell line'),
        ),
        migrations.AlterField(
            model_name='historicalmammalianline',
            name='culture_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='Culture type'),
        ),
        migrations.AlterField(
            model_name='mammalianline',
            name='culture_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='Culture type'),
        ),
    ]
