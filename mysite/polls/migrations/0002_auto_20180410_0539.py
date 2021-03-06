# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-10 05:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=datetime.datetime(2018, 4, 10, 5, 39, 22, 181282, tzinfo=utc), max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=0, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
