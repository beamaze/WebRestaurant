# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 05:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='prices',
            new_name='price',
        ),
    ]
