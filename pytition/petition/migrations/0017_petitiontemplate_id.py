# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-30 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0016_auto_20181027_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='petitiontemplate',
            name='id',
            field=models.IntegerField(db_index=True, default=1, unique=True),
            preserve_default=False,
        ),
    ]