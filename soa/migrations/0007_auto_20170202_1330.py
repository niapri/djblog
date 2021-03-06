# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 19:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('soa', '0006_auto_20170201_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='DLWGPB8', editable=False, max_length=10),
        ),
    ]
