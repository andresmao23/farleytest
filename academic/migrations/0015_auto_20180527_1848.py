# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-27 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0014_teacher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]