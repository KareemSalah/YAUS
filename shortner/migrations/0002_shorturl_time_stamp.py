# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='time_stamp',
            field=models.DateField(auto_now=True),
        ),
    ]