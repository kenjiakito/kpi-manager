# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-24 04:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0033_worktime_time_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktime',
            name='rest_time',
        ),
    ]
