# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-25 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0017_auto_20181125_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='created_approval_by_pi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_approval_by_pi',
            field=models.BooleanField(default=False),
        ),
    ]
