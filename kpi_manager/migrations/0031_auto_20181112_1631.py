# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0030_task_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(blank=True, choices=[('NF', 'Chưa Hoàn Thành'), ('PR', 'Đang Thực Hiện'), ('CO', 'Hoàn Thành')], max_length=2, null=True, verbose_name='Trạng Thái'),
        ),
    ]
