# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soa', '0010_auto_20170202_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='ANFVO9U', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('Refi', 'Refinance'), ('Sale', 'Sale')], default='SALE', max_length=8),
        ),
    ]