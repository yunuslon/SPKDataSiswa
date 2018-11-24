# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-03 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0051_auto_20181103_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hasiltes_f',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='hasiltes_k',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='hasiltes_m',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='karakter_f',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='karakter_k',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='karakter_m',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='kelas_f',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='kelas_k',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='kelas_m',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='nilaiakademik_f',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='nilaiakademik_k',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='nilaiakademik_m',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='plomba_f',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='plomba_k',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='plomba_m',
            name='siswa',
        ),
        migrations.RemoveField(
            model_name='siswa_f',
            name='user',
        ),
        migrations.RemoveField(
            model_name='siswa_k',
            name='user',
        ),
        migrations.RemoveField(
            model_name='siswa_m',
            name='user',
        ),
        migrations.DeleteModel(
            name='TesOlimpiade_F',
        ),
        migrations.DeleteModel(
            name='TesOlimpiade_K',
        ),
        migrations.DeleteModel(
            name='TesOlimpiade_M',
        ),
        migrations.DeleteModel(
            name='HasilTes_F',
        ),
        migrations.DeleteModel(
            name='HasilTes_K',
        ),
        migrations.DeleteModel(
            name='HasilTes_M',
        ),
        migrations.DeleteModel(
            name='Karakter_F',
        ),
        migrations.DeleteModel(
            name='Karakter_K',
        ),
        migrations.DeleteModel(
            name='Karakter_M',
        ),
        migrations.DeleteModel(
            name='Kelas_F',
        ),
        migrations.DeleteModel(
            name='Kelas_K',
        ),
        migrations.DeleteModel(
            name='Kelas_M',
        ),
        migrations.DeleteModel(
            name='NilaiAkademik_F',
        ),
        migrations.DeleteModel(
            name='NilaiAkademik_K',
        ),
        migrations.DeleteModel(
            name='NilaiAkademik_M',
        ),
        migrations.DeleteModel(
            name='Plomba_F',
        ),
        migrations.DeleteModel(
            name='Plomba_K',
        ),
        migrations.DeleteModel(
            name='Plomba_M',
        ),
        migrations.DeleteModel(
            name='Siswa_F',
        ),
        migrations.DeleteModel(
            name='Siswa_K',
        ),
        migrations.DeleteModel(
            name='Siswa_M',
        ),
    ]
