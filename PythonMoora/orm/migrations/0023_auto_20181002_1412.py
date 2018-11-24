# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-02 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0022_auto_20180929_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biologi',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='fisika',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='hasiltes_biologi',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='hasiltes_fisika',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='hasiltes_kimia',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='kimia',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='testfisika',
            name='user',
        ),
        migrations.RemoveField(
            model_name='testkimia',
            name='user',
        ),
        migrations.RemoveField(
            model_name='testmatik',
            name='user',
        ),
        migrations.DeleteModel(
            name='Biologi',
        ),
        migrations.DeleteModel(
            name='Fisika',
        ),
        migrations.DeleteModel(
            name='HasilTes_Biologi',
        ),
        migrations.DeleteModel(
            name='HasilTes_Fisika',
        ),
        migrations.DeleteModel(
            name='HasilTes_Kimia',
        ),
        migrations.DeleteModel(
            name='Kimia',
        ),
        migrations.DeleteModel(
            name='testfisika',
        ),
        migrations.DeleteModel(
            name='testkimia',
        ),
        migrations.DeleteModel(
            name='testmatik',
        ),
    ]
