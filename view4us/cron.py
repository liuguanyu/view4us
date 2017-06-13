# -*- coding: utf-8 -*-

import conf
import json
import traceback

from spider import baidu as list_vender 
from spider import dy8 as detail_vender

# 电视剧关键字列表
def get_teleplay_index():
    url_list = conf.LIST_PLAY_INDEX
    list = {}

    for key in url_list:
        node = list_vender.get_list(url_list[key])
        list[key] = node

    json.dump(list, open("/Users/liuguanyu/devspace/view4us/1.json", "w"))

# 电视剧详情
def get_teleplay_detail():
    f = file("/Users/liuguanyu/devspace/view4us/1.json")
    spider_tasks = json.load(f)

    for i in spider_tasks:
        for node in spider_tasks[i]:
            keyword, trend, number = [node[key] for key in ("keyword", "trend", "number")]
            
            detail = detail_vender.get_teleplay_search_list(keyword)
            print detail, i
            #print "\n"

    f.close()