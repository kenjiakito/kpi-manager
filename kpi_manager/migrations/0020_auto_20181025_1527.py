# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0019_auto_20181025_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='department',
        ),
        migrations.AlterField(
            model_name='departmentmember',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='kpi_manager.DepartmentMember', verbose_name='Nhân Viên'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='kpi_manager.DepartmentMember'),
        ),
    ]