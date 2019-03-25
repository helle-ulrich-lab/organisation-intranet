# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-23 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0005_auto_20181120_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('arranged', 'arranged')], default='open', max_length=255, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('arranged', 'arranged')], default='open', max_length=255, verbose_name='Status'),
        ),
    ]
