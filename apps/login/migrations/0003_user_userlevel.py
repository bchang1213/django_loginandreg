# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-27 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userlevel',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]
