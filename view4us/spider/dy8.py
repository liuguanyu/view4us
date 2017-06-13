# -*- coding: utf-8 -*-

from urllib import quote
from view4us import utils

SEARCH_URL = "http://www.dy8.tv/?s=%s"

def get_search_url(keyword):
    return SEARCH_URL % quote(keyword.encode('utf-8')) 

def get_ext_info(url):
    soup = utils.get_html(url)
    content = soup.find("div", {"id", "main"})

    return content

def get_teleplay_search_list(keyword):
    soup = utils.get_html(get_search_url(keyword))
    content = soup.find("div", {"class", "post-wrap"})

    if content is None:
        return []

    list = content.find_all("div", {"class", "post"})

    if list is None:
        return []

    def _get_node_info(x):
        info = {}

        info["title"] = x.find("h2", {"class": "title"}).find("a").get_text()
        info["desc_url"] = x.find("h2", {"class": "title"}).find("a")["href"]       
        info["update_date"] = x.find("span", {"class": "meta_date"}).get_text().encode("utf-8").replace("更新时间：", "")    
        
        pic = x.find("img", {"class": "wp-post-image"})
        info["pic"] = pic["data-lazy-src"] if not pic["data-lazy-src"] is None else pic["src"]
        
        ext = get_ext_info(info["desc_url"])

        return info

    return map(lambda x: _get_node_info(x), list)
