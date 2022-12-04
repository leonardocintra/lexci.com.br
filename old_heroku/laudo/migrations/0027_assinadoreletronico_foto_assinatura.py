# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-29 12:24
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0026_remove_assinadoreletronico_foto_assinatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinadoreletronico',
            name='foto_assinatura',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagem'),
        ),
    ]