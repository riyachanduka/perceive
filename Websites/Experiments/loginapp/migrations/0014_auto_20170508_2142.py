# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0013_auto_20170508_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailthread',
            name='child_email',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_email', to='loginapp.EmailBody'),
        ),
    ]
