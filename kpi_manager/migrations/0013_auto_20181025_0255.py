# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0012_auto_20181025_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentmember',
            name='position',
            field=models.CharField(blank=True, default='Nhân Viên', max_length=225, null=True, verbose_name='Chức Vụ'),
        ),
    ]
