# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0021_auto_20181025_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='worktime',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='worktime',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
