# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0023_auto_20181025_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
