# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-21 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_account_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='group',
        ),
    ]