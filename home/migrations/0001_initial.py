# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=70)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=14)),
            ],
        ),
    ]
