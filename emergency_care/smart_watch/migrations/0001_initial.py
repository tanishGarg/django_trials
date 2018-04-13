# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Care_givers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('care_giver_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Watch_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_beat', models.IntegerField(default=0)),
                ('step', models.IntegerField(default=0)),
                ('distance', models.IntegerField(default=0)),
                ('hospital', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('person', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='smart_watch.Person_information')),
            ],
        ),
        migrations.AddField(
            model_name='care_givers',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_watch.Person_information'),
        ),
    ]
