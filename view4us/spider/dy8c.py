# -*- coding: utf-8 -*-

from urllib import quote
from view4us import utils

import re

import traceback

SEARCH_URL = "http://www.dy8c.com/?s=%s"
LIST_URL = "http://www.dy8c.com/page/%s/"
HOME_URL = "http://www.dy8c.com/" 

DOWNLOAD_LEADING_TEXT = "与您分享以下搜索自互联网的资源，仅供学习："

def get_search_url(keyword):
    return SEARCH_URL % quote(keyword.encode('utf-8'))  

def _get_node_type(soup):
    content = soup.find("h1", {"class", "title"})

    if content is None:
        return ""

    span = content.find("span")

    if span is None:
        return "movie"

    text = span.get_text().encode('utf-8')

    if re.search(r'全集', text):
        return "tv"

    if re.search(r'更新到(\d+)集', text):
        return "tv"

    if re.search(r'更新到(\d+)期', text):
        return "show"

    if re.search(r'清', text):
        return "movie"    

    if re.search(r'(\d+)P', text):
        return "movie"           

    return "movie"

def _get_desc_in_detail(soup):
    content = soup.find("div", {"class", "wp-caption"})

    if content is None:
        return ""

    desc = []

    while content.find_next_sibling().name == "p":
        node = content.find_next_sibling()
        desc.append(node.get_text())
        content = node

    return "\n".join(desc) 

# 下载链接源码分类：
# 1、多pa型：每一个链接一个<p><a>
# 2、p+table型：每组链接，以<p>开始，以table为主要内容，其中每个链接包含一个链接（如果
#    种下载方式、则N个链接）
def _get_download_code_type(title_dom):
    print title_dom.find_next_sibling().contents[0], title_dom.find_next_sibling().contents[0].name
    if title_dom.find_next_sibling().contents[0].name == "a":
        return "mpa"

    if title_dom.find_next_sibling().find_next_sibling().name == "table":
        return "ptbl"    

def _get_ptbl_urls(title_dom):
    tbl = title_dom.find_next_sibling().find_next_sibling()
    trs = tbl.find_all("tr", {"class": ["el-s-tr1", "el-s-tr2"]})

    def _get_real_links(x):
        links = x.find_all("a")

        return {
            "e2dk": links[0]["href"],
            "thunder": links[1]["href"]
        };
    
    return map(lambda x: _get_real_links(x), trs)  

def _get_mpa_urls(title_dom):
    return []     

def _get_download_urls(soup):
    leading_dom = soup.find(text=DOWNLOAD_LEADING_TEXT)

    if leading_dom is None:
        return []

    leading_dom = leading_dom.parent
    download_hint_titles = leading_dom.find_next_siblings("h3")

    download_urls = []
    for title_dom in download_hint_titles:
        title = title_dom.get_text().encode("utf-8").strip("：")

        link_type = _get_download_code_type(title_dom)
        links = eval("_get_" + link_type + "_urls")(title_dom)
        
        download_urls.append({
            "title": title,
            "links": links
        })

    return download_urls

def _get_ext_info(url):
    soup = utils.get_html(url)

    return {
        "desc": _get_desc_in_detail(soup),
        "type": _get_node_type(soup),
        "download_urls": _get_download_urls(soup)
    }

def _get_node_info(x):
    info = {}

    try:
        info["title"] = x.find("h2", {"class": "title"}).find("a").get_text().encode("utf-8")
        info["desc_url"] = x.find("h2", {"class": "title"}).find("a")["href"]       
        info["update_date"] = x.find("span", {"class": "meta_date"}).get_text().encode("utf-8").replace("更新时间：", "")    
        
        pic = x.find("img", {"class": "wp-post-image"})
        info["pic"] = pic["data-lazy-src"] if not pic["data-lazy-src"] is None else pic["src"]
        
        ext = _get_ext_info(info["desc_url"]) 

        info["desc"] = ext["desc"].encode("utf-8") if not ext["desc"] is None else ""
        info["type"] = ext["type"] if not ext["type"] is None else ""
        info["download_urls"] = ext["download_urls"] if not ext["download_urls"] is None else []
        
        print info["title"], info["desc_url"], info["type"], info["download_urls"]
    except Exception, e:
        traceback.print_exc()   

    return info    

def get_teleplay_search_list(keyword):
    soup = utils.get_html(get_search_url(keyword))
    content = soup.find("div", {"class", "post-wrap"})

    if content is None:
        return []

    list = content.find_all("div", {"class", "post"})

    if list is None:
        return []

    return map(lambda x: _get_node_info(x), list)

def get_recent_list(page = 1):
    list_url = LIST_URL % str(page)
    soup = utils.get_html(list_url)

    content = soup.find(id="content")
    
    if content is None:
        return []

    list = content.find_all("div", {"class", "post-box"})

    if list is None:
        return []

    return map(lambda x: _get_node_info(x), list)

def get_all_page():
    soup = utils.get_html(HOME_URL)
    pages = soup.find_all("a", {"class", "page-numbers"})

    if pages is None or len(pages) == 0 :
        return 1

    pages = filter(lambda x: x != "下页",
        map(lambda x: x.get_text().strip().encode("utf-8"), pages)
    )

    return int(re.compile('第|页|,').sub("", pages[-1]).strip())