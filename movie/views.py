# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
# from django.core import serializers

from video.models import Video
from view4us import utils


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def detail(request, movie_id):
#     return HttpResponse("This is a detail page %s." % movie_id)


def detail(request, movie_id):
    movie = get_object_or_404(Video, pk=movie_id)

    movie = utils.split_field_on_object(movie, ["categories", "directors", "scripters", "performers"])

    return render(request, 'detail.html', {
        'movie': movie
    })
