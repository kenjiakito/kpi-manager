# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0029_auto_20181031_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.CharField(blank=True, choices=[('NF', 'Chưa Hoàn Thành'), ('PR', 'Đang Thực Hiện'), ('CO', 'Hoàn Thành')], default='PR', max_length=2, null=True, verbose_name='Trạng Thái'),
        ),
    ]
