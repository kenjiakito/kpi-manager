# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_manager', '0006_auto_20181025_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='value',
            new_name='target_value',
        ),
        migrations.AddField(
            model_name='comment',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='removed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='worktime',
            name='removed',
            field=models.BooleanField(default=False),
        ),
    ]
