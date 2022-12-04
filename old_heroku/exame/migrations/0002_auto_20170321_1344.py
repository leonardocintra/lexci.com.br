# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exame', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exame',
            options={'ordering': ['descricao'], 'verbose_name': 'Exame do Laudo', 'verbose_name_plural': 'Exames do Laudo'},
        ),
        migrations.AlterField(
            model_name='exame',
            name='descricao',
            field=models.CharField(max_length=200, unique=True, verbose_name='Descrição'),
        ),
    ]