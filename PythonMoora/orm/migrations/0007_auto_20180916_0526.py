# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-16 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0006_auto_20180915_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akademik',
            name='nama',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='akademik',
            name='nilai',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='siswa',
            name='alamat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='siswa',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='siswa',
            name='nama',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
