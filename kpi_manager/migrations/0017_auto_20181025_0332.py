# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0016_auto_20181025_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='kpi_manager.Profile'),
        ),
    ]