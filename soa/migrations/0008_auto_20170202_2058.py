# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soa', '0007_auto_20170202_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed_by',
            field=models.CharField(choices=[('JBLE', 'Jamie Bledsoe'), ('BWI', 'Brandy Wills'), ('BBA', 'Brittany Backman'), ('MFO', 'Micaela Fouda'), ('EGL', 'Elisha Glover'), ('NWA', 'Natasha Wawr?')], default='ANON', max_length=4),
        ),
        migrations.AddField(
            model_name='order',
            name='division',
            field=models.CharField(choices=[('SATX', 'San Antonio'), ('ATX', 'Austin'), ('HTX', 'Houston'), ('DTX', 'Dallas'), ('MTX', 'Midland'), ('LTX', 'Laredo'), ('CCTX', 'Corpus Christi')], default='NONE', max_length=4),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='JRPTBE4', editable=False, max_length=10),
        ),
    ]