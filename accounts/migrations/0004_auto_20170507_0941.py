# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 13:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170506_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_birth',
            field=models.DateField(default=datetime.datetime(2017, 5, 7, 9, 41, 36, 340335)),
        ),
    ]