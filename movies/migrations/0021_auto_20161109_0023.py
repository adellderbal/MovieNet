# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 22:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_auto_20161029_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='production_role',
            new_name='production_roles',
        ),
    ]
