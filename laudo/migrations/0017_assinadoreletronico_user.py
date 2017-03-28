# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 00:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laudo', '0016_remove_assinadoreletronico_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinadoreletronico',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]