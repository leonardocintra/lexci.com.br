# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0028_tipoexame'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoExame',
        ),
    ]