# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApp', '0004_auto_20160813_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualbook',
            name='actualbookTitle',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='categoryName',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
