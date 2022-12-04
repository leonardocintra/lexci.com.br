# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0005_examelaudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='laudo',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='laudo',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='laudo',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]