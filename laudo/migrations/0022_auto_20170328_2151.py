# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-29 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laudo', '0021_assinadoreletronico_foto_assinatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assinadoreletronico',
            name='foto_assinatura',
            field=models.ImageField(null=True, upload_to='laudo/media/', verbose_name='Assinatura'),
        ),
    ]
