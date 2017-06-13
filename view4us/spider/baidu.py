# -*- coding: utf-8 -*-

from view4us import utils

def get_list(url):
    soup = utils.get_html(url, "gb18030")
    tbl = soup.find("table", {"class", "list-table"})

    list = tbl.find_all("tr")[1:]
    
    def _get_node_info(x):
        info = {}

        title = x.find("a", {"class": "list-title"})
        info["keyword"] = title.get_text() if not title is None else ""

        number = x.find("td", {"class": "last"})
        info["number"] = int(number.get_text()) if not number is None else ""
        
        icon = number.find("span")["class"][0].replace('icon-', '') if not number is None else ""     
        info["trend"] = icon

        return info

    return filter(lambda x: x["keyword"] != "",
        map(lambda x: _get_node_info(x), list))    