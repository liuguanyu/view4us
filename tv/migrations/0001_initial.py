# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pic', models.URLField(max_length=255)),
                ('desc_url', models.URLField(max_length=255)),
                ('desc', models.TextField()),
                ('update_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
