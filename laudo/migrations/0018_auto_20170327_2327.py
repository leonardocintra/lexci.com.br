# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0017_assinadoreletronico_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laudo',
            name='assinado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assinador', to='laudo.AssinadorEletronico'),
        ),
    ]
