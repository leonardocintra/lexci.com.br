# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0036_auto_20170810_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laudo',
            name='ultima_menstruacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data ultima menstruação'),
        ),
    ]