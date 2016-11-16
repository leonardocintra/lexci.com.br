# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cartao_sus', models.CharField(max_length=15, unique=True, verbose_name='SUS')),
                ('name_mae', models.CharField(max_length=150, verbose_name='Nome da mãe')),
                ('apelido', models.CharField(blank=True, max_length=100, null=True)),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('nacionalidade', models.CharField(default='brasileira', max_length=100)),
                ('data_nascimento', models.DateField()),
                ('raca', models.CharField(choices=[('BRA', 'Branca'), ('PRE', 'Preta'), ('PAR', 'PARDA'), ('AMA', 'Amarela'), ('IND', 'Indigena / Etinia'), ('OUT', 'Outra')], default='BRA', max_length=3, verbose_name='Raça')),
            ],
            options={
                'verbose_name': 'Paciente',
                'ordering': ['nome'],
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='PacienteEndereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero_casa', models.CharField(blank=True, max_length=10, null=True, verbose_name='Nº')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('codigo_municipio', models.IntegerField(verbose_name='Codigo Municipio')),
                ('municipio', models.CharField(blank=True, max_length=100, null=True)),
                ('cep', models.CharField(max_length=8)),
                ('fone_ddd', models.CharField(max_length=2)),
                ('fone_numero', models.CharField(max_length=11)),
                ('ponto_de_referencia', models.CharField(blank=True, max_length=100, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]