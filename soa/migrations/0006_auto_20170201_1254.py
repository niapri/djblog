# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soa', '0005_auto_20170131_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='LXS50FA', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
