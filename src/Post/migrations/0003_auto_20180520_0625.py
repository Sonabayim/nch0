# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20180520_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
