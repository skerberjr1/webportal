# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-23 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_account_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='department',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
