# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0023_auto_20170810_0842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('order',)},
        ),
        migrations.RemoveField(
            model_name='client',
            name='priority',
        ),
    ]