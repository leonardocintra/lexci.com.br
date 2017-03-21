# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemExame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_item', models.CharField(max_length=300, verbose_name='Descrição')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('exame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exame', to='exame.Exame')),
            ],
            options={
                'verbose_name': 'Item exame',
                'verbose_name_plural': 'Itens dos Exame',
                'ordering': ['descricao_item'],
            },
        ),
    ]
