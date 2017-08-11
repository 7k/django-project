# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0011_auto_20170809_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='page',
            name='testimonials',
        ),
        migrations.AddField(
            model_name='client',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolios.Page'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolios.Page'),
        ),
    ]