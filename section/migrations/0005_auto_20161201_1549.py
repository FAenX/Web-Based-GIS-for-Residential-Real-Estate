# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-01 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0004_auto_20161201_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='baths',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')]),
        ),
    ]
