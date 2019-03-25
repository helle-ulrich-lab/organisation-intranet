# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-26 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0018_auto_20181125_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='status',
            field=models.CharField(blank=True, choices=[('submitted', 'submitted'), ('open', 'open'), ('arranged', 'arranged'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='submitted', max_length=255, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('submitted', 'submitted'), ('open', 'open'), ('arranged', 'arranged'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='submitted', max_length=255, verbose_name='Status'),
        ),
    ]
