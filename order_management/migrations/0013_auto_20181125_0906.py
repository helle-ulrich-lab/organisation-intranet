# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-25 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0012_auto_20181124_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='created_approval_by_pi',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='created_approval_by_pi',
            field=models.BooleanField(default='True'),
            preserve_default=False,
        ),
    ]
