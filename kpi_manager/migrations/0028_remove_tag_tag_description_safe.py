# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 07:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0027_auto_20181031_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_description_safe',
        ),
    ]
