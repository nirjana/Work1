# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-05 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20181205_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='done_by',
            old_name='done_by',
            new_name='t_name',
        ),
    ]
