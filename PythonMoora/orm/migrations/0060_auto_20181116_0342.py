# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-16 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0059_auto_20181114_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siswa',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki - Laki', 'Laki - Laki'), ('Perempuan', 'Perempuan')], default='Laki - Laki', max_length=15),
        ),
    ]