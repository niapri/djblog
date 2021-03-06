# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 02:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateTimeField(default=None)),
                ('completed', models.CharField(default='n', max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField(default=None)),
                ('cad_num', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gf_number', models.CharField(max_length=50)),
                ('title_co', models.CharField(max_length=100)),
                ('preparer', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('current_owner', models.CharField(max_length=100)),
                ('buyer', models.CharField(max_length=100)),
            ],
        ),
    ]
