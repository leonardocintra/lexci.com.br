# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0035_auto_20170809_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laudo',
            name='data_coleta',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da coleta'),
            preserve_default=False,
        ),
    ]