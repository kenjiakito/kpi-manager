# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 08:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0022_auto_20181025_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worktime',
            options={'ordering': ('-date', '-created_at')},
        ),
    ]