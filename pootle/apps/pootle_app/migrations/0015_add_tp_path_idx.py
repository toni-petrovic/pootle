# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-04 16:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_app', '0014_set_directory_tp_path'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='directory',
            index_together=set([('obsolete', 'tp', 'tp_path'), ('obsolete', 'pootle_path')]),
        ),
    ]
