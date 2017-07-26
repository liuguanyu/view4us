# -*- coding: utf-8 -*-

import conf
import json
import traceback

from spider import baidu as list_vender 
from spider import dy8c as detail_vender
from spider import dy8c as recent_vender

from tv.models import Tv
from movie.models import Movie

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
            print detail, keyword, i
            #print "\n"

    f.close()

# 获取最新列表

def get_recent_item():
    for i in xrange(1, recent_vender.get_all_page()):
        list = recent_vender.get_recent_list(i)
        try:
            for node in list:
                if node["type"] == "tv":
                    print node["type"]

                    kargs = {item: node[item] for item in ("title", "desc", "pic", "desc_url")}
                    tv = Tv(**kargs)
                    tv.save()
                # elif node["type"] == "movie":
                #     print node["type"]
                #
                #     kargs = {item: node[item] for item in ("title", "desc", "pic", "desc_url")}
                #     movie = Movie(**kargs)
                #     movie.save()


        except Exception, e:
            traceback.print_exc()