# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-29 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0025_auto_20170328_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assinadoreletronico',
            name='foto_assinatura',
        ),
    ]