# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-24 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0066_auto_20181121_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='tanggal_lahir',
            field=models.DateField(blank=True, null=True),
        ),
    ]
