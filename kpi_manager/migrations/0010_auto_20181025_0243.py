# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0009_auto_20181025_0207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmentmember',
            name='user',
        ),
        migrations.AddField(
            model_name='departmentmember',
            name='department_member',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='kpi_manager.Profile', verbose_name='Thành Viên'),
        ),
    ]
