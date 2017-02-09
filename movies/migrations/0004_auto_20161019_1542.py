# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20161019_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='movies_list', to='movies.Person', verbose_name='list of actors'),
        ),
    ]
