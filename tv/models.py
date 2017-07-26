# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tv(models.Model):
    title = models.CharField(max_length=255)
    pic = models.URLField(max_length=255)
    desc_url = models.URLField(max_length=255)
    desc = models.TextField()
    update_date = models.DateTimeField(auto_now=True)