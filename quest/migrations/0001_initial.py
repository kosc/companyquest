# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-02 16:22
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bid', models.FloatField()),
                ('bid_type', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('bid_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=3), size=None)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Channel'),
        ),
    ]
