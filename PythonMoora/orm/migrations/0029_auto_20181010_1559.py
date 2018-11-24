# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-10 15:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orm', '0028_tesolimpiade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siswa',
            name='user',
        ),
        migrations.AddField(
            model_name='tesolimpiade',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tesolimpiades', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
