# -*- coding: utf-8 -*-

import urllib.request
import random
import ast
from bs4 import BeautifulSoup

from view4us import conf


def get_fake_headers():
    return conf.HEADERS[random.randint(0, len(conf.HEADERS)-1)]


def retry_http(func):
    def handle(*args, **kwargs):
        max_retry = conf.MAX_RETRY
        
        ret = ""

        while ret == "" and max_retry > 0:
            try:
                ret = func(*args, **kwargs)
            except (urllib.error.HTTPError, urllib.error.URLError) as e:
                pass
            except Exception as e:
                print(e)
                max_retry -= 1

        return ret

    return handle    


@retry_http
def get_html(url, source_charset="utf-8"):
    req = urllib.request.Request(url, headers=get_fake_headers())
    source_code = urllib.request.urlopen(req, timeout=10).read()
    return BeautifulSoup(source_code, "lxml", from_encoding=source_charset)


def split_field_on_object(obj, fields):
    for field in fields:
        setattr(obj, field, getattr(obj, field).split(" "))

    return obj


def json_field_on_object(obj, fields):
    for field in fields:
        setattr(obj, field, ast.literal_eval(getattr(obj, field)))

    return obj
