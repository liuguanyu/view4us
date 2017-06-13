# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def get_list():
        pass