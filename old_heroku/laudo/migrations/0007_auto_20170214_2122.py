# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-14 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0006_auto_20170211_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laudo',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='paciente.Paciente'),
        ),
    ]