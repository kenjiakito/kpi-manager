# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0020_auto_20181025_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='kpi_manager.DepartmentMember'),
        ),
    ]
