# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soa', '0037_auto_20170205_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='5DGOGC3', editable=False, max_length=10),
        ),
    ]