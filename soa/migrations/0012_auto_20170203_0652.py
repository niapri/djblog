# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soa', '0011_auto_20170202_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='2Q2XU69', editable=False, max_length=10),
        ),
    ]
