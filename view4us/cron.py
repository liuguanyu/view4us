# -*- coding: utf-8 -*-

import conf
import json
import traceback

from spider import baidu as list_vender
from spider import dy8c as recent_vender

from video.models import Video
from movie.models import Movie

# 电视剧关键字列表
def get_teleplay_index():
    url_list = conf.LIST_PLAY_INDEX
    list = {}

    for key in url_list:
        node = list_vender.get_list(url_list[key])
        list[key] = node

    json.dump(list, open("/Users/liuguanyu/devspace/view4us/1.json", "w"))

# 获取最新列表
def get_recent_item():
    for i in xrange(1, recent_vender.get_all_page()):
        list = recent_vender.get_recent_list(i)
        try:
            for node in list:
                video = Video(**node)
                video.save()
        except Exception, e:
            traceback.print_exc()