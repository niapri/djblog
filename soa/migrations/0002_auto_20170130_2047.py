# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(max_length=15),
        ),
    ]
