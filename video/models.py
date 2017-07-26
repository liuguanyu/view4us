# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    pic = models.URLField(max_length=255)
    category = models.URLField(max_length=255)

    performers = models.TextField()
    directors = models.TextField()
    scripters = models.TextField()

    imdb = models.CharField(max_length=255)
    download_urls = models.TextField()

    desc = models.TextField()

    language = models.TextField()

    first_show = models.CharField(max_length=255)
    area = models.CharField(max_length=255)

    desc_url = models.URLField(max_length=255)
    update_date = models.DateTimeField(auto_now=True)