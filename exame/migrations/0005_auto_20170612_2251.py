# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 01:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exame', '0004_auto_20170403_2112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exame',
            new_name='TipoExame',
        ),
    ]