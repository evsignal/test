# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_actor_real_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='biography',
            field=models.TextField(null=True),
        ),
    ]
