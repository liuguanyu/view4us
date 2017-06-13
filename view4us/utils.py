# -*- coding: utf-8 -*-

import urllib2
import random
from bs4 import BeautifulSoup

import conf

def get_fake_headers():
    return conf.HEADERS[random.randint(0, len(conf.HEADERS)-1)]

def retry_http(func):
    def handle(*args, **kwargs):
        max_retry = conf.MAX_RETRY
        print "in decorator"
        
        ret = ""

        while ret == "" and max_retry > 0:
            try:
                ret = func(*args, **kwargs)
            except (urllib2.HTTPError, urllib2.URLError), e:
                pass
            except Exception, e:
                max_retry -= 1

        return ret

    return handle    

@retry_http
def get_html(url, source_charset="utf-8"):
    req = urllib2.Request(url, headers=get_fake_headers())
    source_code = urllib2.urlopen(req, timeout=10).read()
    return BeautifulSoup(source_code, "lxml", from_encoding=source_charset)