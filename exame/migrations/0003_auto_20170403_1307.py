# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-03 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exame', '0002_auto_20170321_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exame',
            options={'verbose_name': 'Exame do Laudo', 'verbose_name_plural': 'Exames do Laudo'},
        ),
        migrations.AddField(
            model_name='exame',
            name='ordem_exibicao',
            field=models.IntegerField(default=0),
        ),
    ]
