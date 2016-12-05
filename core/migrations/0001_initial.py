# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
            ],
            options={
                'verbose_name': 'Convenios',
                'ordering': ['descricao'],
            },
        ),
    ]
