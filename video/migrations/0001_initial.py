# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('pic', models.URLField(max_length=255)),
                ('category', models.URLField(max_length=255)),
                ('performers', models.TextField()),
                ('directors', models.TextField()),
                ('scripters', models.TextField()),
                ('imdb', models.CharField(max_length=255)),
                ('download_urls', models.TextField()),
                ('desc', models.TextField()),
                ('language', models.TextField()),
                ('first_show', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('desc_url', models.URLField(max_length=255)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
